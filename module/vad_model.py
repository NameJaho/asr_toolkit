from funasr import AutoModel

model = AutoModel(model="fsmn-vad")
wav_file = "../output/audios/rubbish.wav"
res = model.generate(input=wav_file)
print(res)