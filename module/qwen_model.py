from funasr import AutoModel

model = AutoModel(model="Qwen-Audio")

audio_in = "output/audios/消费50-240306_久谦咨询_电商GMV广告项目_字节跳动_大众消费总监_刘先生专家访谈.wav"
prompt = "<|startoftranscription|><|en|><|transcribe|><|en|><|notimestamps|><|wo_itn|>"

res = model.generate(input=audio_in, prompt=prompt)
print(res)