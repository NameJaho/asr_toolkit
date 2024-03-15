import numpy as np
import librosa
import librosa.display
from funasr import AutoModel
import tools.my_utils as utils
import os

VAD_MODEL_NAME = "speech_fsmn_vad_zh-cn-16k-common-pytorch"


class WavDetector:
    def __init__(self, audio_path):
        self.audio_path = audio_path
        self.vad_model_path = os.path.join(utils.get_root_path(), "models", VAD_MODEL_NAME)

    def load_audio(self):
        y, sr = librosa.load(self.audio_path)
        return y, sr

    def calculate_mel_spec(self):
        y, sr = self.load_audio()
        mel_spec = librosa.feature.melspectrogram(y=y, sr=sr)
        return mel_spec

    def get_audio_length(self):
        y, sr = self.load_audio()
        #y, sr = librosa.load(self.audio_path, sr=None)
        length_in_seconds = librosa.get_duration(y, sr)
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

    def extract_features(self):
        wav, freq = self.load_audio()

        features = dict()

        features['wav_freq'] = freq
        features['wav_points'] = wav.shape[0]
        features['tempo_bpm'] = librosa.beat.beat_track(y=wav, sr=freq)[0]

        beat_frames = librosa.beat.beat_track(y=wav, sr=freq)[1]
        beat_times = librosa.frames_to_time(beat_frames, sr=freq)
        rolloff_freq = np.mean(librosa.feature.spectral_rolloff(y=wav, sr=freq, hop_length=512, roll_percent=0.9))

        features['avg_diff_beat_times'] = round(np.mean(beat_times[1:] - beat_times[0:len(beat_times) - 1]), 4)
        features['std_diff_beat_times'] = round(np.std(beat_times[1:] - beat_times[0:len(beat_times) - 1]), 4)
        features['rolloff_freq'] = round(rolloff_freq, 0)

        mel_spec = self.calculate_mel_spec()
        # 时域能量分布特征
        features['energy_variation'] = np.std(np.sum(mel_spec, axis=0))

        db20_splits = librosa.effects.split(y=wav, frame_length=4000, top_db=20)
        features['db20_splits_size'] = db20_splits.size

        wav_harm, wav_perc = librosa.effects.hpss(wav)

        features['wav_harm_mean'] = np.mean(wav_harm)
        features['wav_perc_mean'] = np.mean(wav_perc)

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


