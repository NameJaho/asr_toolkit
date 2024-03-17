import librosa
import numpy as np
import warnings
warnings.filterwarnings("ignore")


def get_audio_length(y, sr):
    length_in_seconds = librosa.get_duration(y, sr)
    return length_in_seconds


def analysis(audio, sr):
    # 提取基频 (Fundamental Frequency) 和基频变化
    # f0, voiced_flag, voiced_probs = librosa.pyin(audio, fmin=librosa.note_to_hz('C2'), fmax=librosa.note_to_hz('C7'))
    #pitch_changes = librosa.piptrack(audio, sr=sr)

    # 提取节奏特征
    onset_frames = librosa.onset.onset_detect(audio, sr=sr)
    # tempo, beats = librosa.beat.beat_track(y=audio, sr=sr, hop_length=512)

    # 输出结果
    # print("基频 (Fundamental Frequency):", f0)
    #print("基频变化:", pitch_changes)
    print("节奏帧数:", len(onset_frames)/get_audio_length(audio, sr))
    #print("节奏速度 (Tempo):", tempo)

    #beat_times = librosa.frames_to_time(beats, sr=sr, hop_length=512)

    #print('beats count', len(beats)/get_audio_length(audio, sr))

    # 提取能量 (Energy) 特征
    energy = librosa.feature.rms(audio)

    # 提取谐波结构 (Harmonic Structure) 特征
    #spectral_contrast = librosa.feature.spectral_contrast(audio, sr=sr)

    # 计算特征统计值
    #f0_mean = np.mean(f0)
    energy_mean = np.mean(energy)
    #contrast_mean = np.mean(spectral_contrast)
    #print('f0 mean', f0_mean)
    print('energy_mean', energy_mean)
    print('energy_std', np.std(energy))
    #print('contrast_mean', contrast_mean)

    # 获取音频信号的振幅
    amplitudes = np.abs(audio)
    intensity_changes = np.diff(amplitudes)
    # 计算归一化强度
    normalized_intensity = librosa.feature.rms(y=audio)
    print('amplitudes mean', np.mean(amplitudes))
    print('intensity_changes mean ', np.mean(intensity_changes))
    print('normalized_intensity mean ', np.mean(normalized_intensity))

    # 计算音高稳定性
    onset_env = librosa.onset.onset_strength(audio, sr=sr)
    # 计算音高变化的平均强度
    mean_onset_strength = np.mean(onset_env[onset_frames])
    print(f'音高稳定性的平均 onset 强度： {mean_onset_strength}')

    # 计算动态范围
    dynamic_range = np.max(amplitudes) - np.min(amplitudes)
    print('dynamic_range ', dynamic_range)

    # 计算短时傅里叶变换（STFT）
    D = librosa.stft(audio, hop_length=512)
    # 将STFT转换为幅度谱（功率谱的对数）
    S = librosa.amplitude_to_db(np.abs(D), ref=np.max, top_db=None)
    # 定义高频部分的频率范围
    freqs = librosa.fft_frequencies(sr=sr)
    high_freq_bin_start = np.argmax(freqs > 11000)
    high_freq_bin_end = np.argmax(freqs > 12000)
    # 提取高频部分的能量
    high_freq_energy = np.sum(S[high_freq_bin_start:high_freq_bin_end])
    print(f'高频部分的能量： {high_freq_energy}')
    #spec = np.abs(librosa.stft(y, hop_length=512))
    #spec = librosa.amplitude_to_db(spec, ref=np.max)

    print('----------------\n')

files = ['song_01.wav', 'song_02.wav', 'song_03.wav', 'speech_01.wav', 'speech_02.wav', 'speech_laugh_01.wav', 'speech_music.wav', 'speech_talk_01.wav']
for file in files:
    # 加载音频文件
    print(file)
    audio_path = f'test/files/{file}'
    audio, sr = librosa.load(audio_path)

    analysis(audio, sr)
