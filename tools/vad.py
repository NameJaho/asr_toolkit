import librosa
from funasr import AutoModel


def vad(wav_file):
    model = AutoModel(model="fsmn-vad")
    y, sr = librosa.load(wav_file, sr=None)  # sr=None 确保以原始采样率加载音频

    # 计算音频时长（秒）
    duration_seconds = librosa.get_duration(y=y, sr=sr)

    result = model.generate(input=wav_file)

    t = 0
    for item in result[0]['value']:
        t += item[1] - item[0]
    duration = result[0]['value'].__len__()
    voice_rate = t / (duration_seconds * 1000)
    print(f'音频总时长为:{duration_seconds}')
    print('间断次数:', duration)
    print('人声占比:', voice_rate)
    return duration_seconds, duration, voice_rate


if __name__ == '__main__':
    wav_file = 'local/pure_speak_01.wav'  # 0.3497737556561086
    vad(wav_file)
