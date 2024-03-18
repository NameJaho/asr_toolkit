from funasr import AutoModel

model = AutoModel(model="/Users/liujeru/dev/asr_toolkit/models/speech_fsmn_vad_zh-cn-16k-common-pytorch")
wav_file = "../output/audios/rubbish.wav"
res = model.generate(input=wav_file)
print(res)