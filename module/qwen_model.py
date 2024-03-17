from funasr import AutoModel
# from transformers import AutoModel

model = AutoModel(model="Qwen-Audio")
# model = AutoModel.from_pretrained("C:/Users/admin/.cache/huggingface/hub/Qwen/Qwen-Audio", trust_remote_code=True)

audio_in = "output/audios/消费50-240306_久谦咨询_电商GMV广告项目_字节跳动_大众消费总监_刘先生专家访谈.wav"
prompt = "<|startoftranscription|><|zh|><|transcribe|><|zh|><|notimestamps|><|wo_itn|>"

res = model.generate(input=audio_in, prompt=prompt)
print(res)