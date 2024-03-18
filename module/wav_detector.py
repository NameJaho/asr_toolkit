import numpy as np
import librosa
import librosa.display
from funasr import AutoModel
import tools.utils as utils
from tools.utils import timer
import os
import warnings

warnings.filterwarnings("ignore")
VAD_MODEL_NAME = "speech_fsmn_vad_zh-cn-16k-common-pytorch"


class WavDetector:
    def __init__(self, audio_path):
        self.audio_path = audio_path
        self.vad_model_path = os.path.join(utils.get_root_path(), "models", VAD_MODEL_NAME)
        self.y, self.sr = librosa.load(self.audio_path)
        self.features = {}

    def get_duration(self):
        duration = librosa.get_duration(y=self.y, sr=self.sr)
        self.features['duration'] = duration
        return duration

    @timer
    def check_vocal(self):
        total_length = self.get_duration()

        model = AutoModel(model=self.vad_model_path)
        vocal_chunks = model.generate(input=self.audio_path)

        vocal_duration = 0
        for vocal_chunk in vocal_chunks[0]['value']:
            vocal_duration += vocal_chunk[1] - vocal_chunk[0]

        gaps = vocal_chunks[0]['value'].__len__()
        vocal_pct = vocal_duration / (total_length * 1000)

        self.features['gaps_per_sec'] = gaps/self.get_duration()
        self.features['vocal_duration'] = vocal_duration
        self.features['vocal_pct'] = vocal_pct

        return gaps, vocal_pct

    @timer
    def extract_energy(self):
        """
        Calculate the short-term energy of audio using the librosa.feature.rms function.
        For the human voice during speaking, there is a relatively large fluctuation in energy.
        For the human voice during singing, the fluctuation in energy is relatively stable.
        Returns: features dict.

        """
        energy = librosa.feature.rms(self.y)

        energy_mean = np.mean(energy)
        energy_std = np.std(energy)

        self.features['energy_mean'] = energy_mean
        self.features['energy_std'] = energy_std

        return self.features

    @timer
    def extract_rhythm(self):
        # 提取节奏特征
        onset_frames = librosa.onset.onset_detect(self.y, sr=self.sr)
        rhythm_per_sec = len(onset_frames) / self.get_duration()
        self.features['rhythm_per_sec'] = rhythm_per_sec
        return self.features

    @timer
    def extract_db20_splits(self):
        db20_splits = librosa.effects.split(y=self.y, frame_length=4000, top_db=20)
        self.features['db20_splits_size'] = db20_splits.size/self.get_duration()
        return self.features

    def extract_features(self):
        self.get_duration()
        self.extract_db20_splits()
        self.extract_energy()
        self.extract_rhythm()

        self.check_vocal()

        return self.features


if __name__ == '__main__':
    wav_detector = WavDetector('../test/files/speech_01.wav')

    gaps, vocal_pct = wav_detector.check_vocal()

    features = wav_detector.extract_features()

    print(wav_detector.features)
