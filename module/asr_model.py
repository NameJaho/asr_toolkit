from funasr import AutoModel
from loguru import logger

# voice recognition model
ASR_MODEL_NAME = "damo/speech_paraformer-large_asr_nat-zh-cn-16k-common-vocab8404-pytorch"
# voice end-point detection model
VAD_MODEL_NAME = "damo/speech_fsmn_vad_zh-cn-16k-common-pytorch"
# punctuation model
PUNC_MODEL_NAME = "damo/punc_ct-transformer_zh-cn-common-vocab272727-pytorch"


class ASRModel:
    def __init__(self):
        self.model = self.get_model()

    @staticmethod
    def get_model():
        model = AutoModel(
            # model='models/speech_paraformer-large-campplus-vad-punc-spk_asr_nat-zh-cn',
            model=ASR_MODEL_NAME, model_revision="v2.0.4",
            vad_model=VAD_MODEL_NAME, vad_model_revision="v2.0.4",
            punc_model=PUNC_MODEL_NAME, punc_model_revision="v2.0.4",
            device='cuda:0'
            # spk_model="cam++", spk_model_revision="v2.0.2",
        )

        # model = AutoModel(model="paraformer-zh", vad_model="fsmn-vad", punc_model="ct-punc-c",
        #                   # spk_model="cam++",
        #                   )
        return model

    # inference param: batch_size_token = 5000, batch_size_token_threshold_s = 40, max_single_segment_time = 6000
    def inference(self, audio_input):
        # model = self.get_model()
        # result = model.generate(audio_input)[0]['text']

        result = self.model.generate(input=audio_input, batch_size=64)
        logger.info(f"{audio_input}  ASR result: {result}")
        if result:
            result = result[0]['text']
        else:
            logger.error("ASR result is None")
            result = ''
        return result


if __name__ == '__main__':
    audio_path = '/Users/jaho/Jaho/Job/asr_toolkit/local/799.wav'
    asr = ASRModel()
    result = asr.inference(audio_path)
    print(result)

    # from funasr import AutoModel

    # paraformer-zh is a multi-functional asr model
    # use vad, punc, spk or not as you need
    # model = AutoModel(model="paraformer-zh", vad_model="fsmn-vad", punc_model="ct-punc",
    #                   # spk_model="cam++"
    #                   )
    # # res = model.generate(input=f"/Users/jaho/Jaho/Job/asr_toolkit/test/xhs3000/2565.wav",
    # res = model.generate(input=f"/Users/jaho/Jaho/Job/asr_toolkit/test/dy/79.wav",
    #                      batch_size_s=300,
    #                      hotword='农夫山泉创始人钟睒睒')  # 创始人钟闪闪
    # print(res)
