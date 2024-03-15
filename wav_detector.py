import numpy as np
import librosa
import librosa.display
from funasr import AutoModel
import tools.my_utils as utils
import os

VAD_MODEL_NAME = "speech_fsmn_vad_zh-cn-16k-common-pytorch"

# Define all major scales to be used later for finding key signature
# Arrays all in the format:  [C, C#, D, Eb, E, F, F#, G, Ab, A, Bb, B]
major_scales = {'C': [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
                'C#': [1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0],
                'D': [0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
                'Eb': [1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0],
                'E': [0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1],
                'F': [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0],
                'F#': [0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1],
                'G': [1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
                'Ab': [1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0],
                'A': [0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
                'Bb': [1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0],
                'B': [0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1]}


class WavDetector:
    def __init__(self, audio_path):
        self.audio_path = audio_path
        self.vad_model_path = os.path.join(utils.get_root_path(), "models", VAD_MODEL_NAME)
        self.y, self.sr = librosa.load(self.audio_path)

    def calculate_mel_spec(self):
        mel_spec = librosa.feature.melspectrogram(y=self.y, sr=self.sr)
        return mel_spec

    def get_audio_length(self):
        length_in_seconds = librosa.get_duration(y=self.y, sr=self.sr)
        return length_in_seconds

    def check_vocal(self):
        model = AutoModel(model=self.vad_model_path)

        total_length = self.get_audio_length()
        vocal_chunks = model.generate(input=self.audio_path)

        vocal_chunk_length = 0
        for vocal_chunk in vocal_chunks[0]['value']:
            vocal_chunk_length += vocal_chunk[1] - vocal_chunk[0]

        gaps = vocal_chunks[0]['value'].__len__()
        vocal_pct = vocal_chunk_length / (total_length * 1000)

        return gaps, vocal_pct

    def get_tempo_gram(self):
        """
        The tempo gram visualizes the rhythm (pattern recurrence), using the
        onset envelope, oenv, to determine the start points for the patterns.
        """
        oenv = librosa.onset.onset_strength(y=self.y, sr=self.sr, hop_length=512)
        tempo_gram = librosa.feature.tempogram(onset_envelope=oenv, sr=self.sr, hop_length=512)
        return tempo_gram

    def find_tonic_and_key(self):
        """
        The tonic is the base note in the key signature, e.g. c is the tonic for
        the key of c major.  The tonic can be found by summing the chromagram
        arrays and finding the index of the array with the greatest sum.  The
        logic is that the tonic is the note with the greatest presence.

        If the tonic doesn't match the tonic of bestmatch, the highest
        correlated major scale, then the key is a minor scale.
        (Minor scales = Major scales but have different tonics)
        """
        chroma_gram = librosa.feature.chroma_stft(y=self.y, sr=self.sr)
        chroma_sums = []
        for i, a in enumerate(chroma_gram):
            chroma_sums.append(np.sum(chroma_gram[i]))
        tonic_val = np.where(max(chroma_sums) == chroma_sums)[0][0]
        notes = ['C', 'C#', 'D', 'Eb', 'E', 'F', 'F#', 'G', 'Ab', 'A', 'Bb', 'B']
        tonic = notes[tonic_val]
        # In standard units, how far is the average pitch from the tonic?
        z_dist_avg_to_tonic = round((max(chroma_sums) - np.mean(chroma_sums)) / np.std(chroma_sums), 4)
        # Correlate the chroma sums array with each of the major scales, find the best match
        best_match = 0
        best_match_id = 0
        for key, scale in major_scales.items():
            # np.corrcoef returns a matrix, only need the first value in the diagonal
            corr = np.corrcoef(scale, chroma_sums)[0, 1]
            if corr > best_match:
                best_match = corr
                best_match_id = key
        if tonic != best_match_id:
            key_sig = tonic + ' Minor'
        else:
            key_sig = tonic + ' Major'
        return tonic, key_sig, z_dist_avg_to_tonic

    def extract_features(self):
        wav, freq = self.y, self.sr

        features = dict()

        features['wav_freq'] = freq
        features['wav_points'] = wav.shape[0]
        features['tempo_bpm'] = librosa.beat.beat_track(y=wav, sr=freq)[0]

        # beat_frames = librosa.beat.beat_track(y=wav, sr=freq)[1]
        # beat_times = librosa.frames_to_time(beat_frames, sr=freq)
        # rolloff_freq = np.mean(librosa.feature.spectral_rolloff(y=wav, sr=freq, hop_length=512, roll_percent=0.9))
        #
        # features['avg_diff_beat_times'] = round(np.mean(beat_times[1:] - beat_times[0:len(beat_times) - 1]), 4)
        # features['std_diff_beat_times'] = round(np.std(beat_times[1:] - beat_times[0:len(beat_times) - 1]), 4)
        # features['rolloff_freq'] = round(rolloff_freq, 0)

        mel_spec = self.calculate_mel_spec()
        # 时域能量分布特征
        features['energy_variation'] = np.std(np.sum(mel_spec, axis=0))

        db20_splits = librosa.effects.split(y=wav, frame_length=4000, top_db=20)
        features['db20_splits_size'] = db20_splits.size

        # wav_harm, wav_perc = librosa.effects.hpss(wav)

        # features['wav_harm_mean'] = np.mean(wav_harm)
        # features['wav_perc_mean'] = np.mean(wav_perc)
        #
        # features['avg_onset_strength'] = round(np.mean(self.get_tempo_gram()), 4)
        # features['std_onset_strength'] = round(np.std(self.get_tempo_gram()), 4)

        # features['tonic'] = self.find_tonic_and_key()[0]
        # features['key_signature'] = self.find_tonic_and_key()[1]
        # features['z_dist_avg_to_tonic'] = self.find_tonic_and_key()[2]

        # Compute the first-order difference of the mel spectrogram
        delta_mel_spec = np.diff(mel_spec, axis=0)

        # Compute the second-order difference of the mel spectrogram
        delta2_mel_spec = np.diff(delta_mel_spec, axis=0)

        # Extract the pitch changes
        pitch_changes = np.argmax(delta2_mel_spec, axis=0)
        # Remove the zero values from the pitch changes array
        pitch_changes = pitch_changes[pitch_changes != 0]

        # Convert the pitch changes to pitch values (in semitones)
        pitch_values = librosa.hz_to_midi(self.sr * pitch_changes)
        print(pitch_values)
        from scipy.signal import savgol_filter
        # Smooth the pitch values
        smoothed_pitch_values = savgol_filter(pitch_values, window_length=11, polyorder=3)

        # Compute the standard deviation of the smoothed pitch values
        std_pitch_change = np.std(smoothed_pitch_values)

        features['std_pitch_change'] = std_pitch_change
        return features


if __name__ == '__main__':
    wav_detector = WavDetector('local/pure_speak_01.wav')
    features = wav_detector.extract_features()

    # step 1
    print('total length: ', wav_detector.get_audio_length())

    # step 2
    print('gaps: ', wav_detector.check_vocal()[0])
    print('vocal pct: ', wav_detector.check_vocal()[1])

    # step 3
    print(features)
