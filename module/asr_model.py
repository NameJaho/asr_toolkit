from funasr import AutoModel


# voice recognition model
ASR_MODEL_NAME = "damo/speech_paraformer-large_asr_nat-zh-cn-16k-common-vocab8404-pytorch"
# voice end-point detection model
VAD_MODEL_NAME = "damo/speech_fsmn_vad_zh-cn-16k-common-pytorch"
# punctuation model
PUNC_MODEL_NAME = "damo/punc_ct-transformer_zh-cn-common-vocab272727-pytorch"


class ASRModel:
    def __init__(self):
        pass

    @staticmethod
    def get_model():
        model = AutoModel(model='yeyupiaoling/speech_paraformer-large-campplus-vad-punc-spk_asr_nat-zh-cn',
            #model=ASR_MODEL_NAME, model_revision="v2.0.4",
                          vad_model=VAD_MODEL_NAME, vad_model_revision="v2.0.4",
                          punc_model=PUNC_MODEL_NAME, punc_model_revision="v2.0.4",
                          #spk_model="cam++", spk_model_revision="v2.0.2",
                          )

        # model = AutoModel(model="paraformer-zh", vad_model="fsmn-vad", punc_model="ct-punc-c",
        #                   # spk_model="cam++",
        #                   )
        return model

    # inference param: batch_size_token = 5000, batch_size_token_threshold_s = 40, max_single_segment_time = 6000
    def inference(self, audio_input):
        model = self.get_model()
        #result = model.generate(audio_input)[0]['text']

        result = model.generate(input=audio_input, batch_size=64)
        return result
