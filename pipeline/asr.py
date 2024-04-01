import argparse
import json
import time
from threading import Thread

import librosa

from api.rds import get_redis, rpush
from module.asr_model import ASRModel

rds = get_redis()

asr_model = ASRModel()


def asr():
    while True:
        datas = rds.lpop('asr_queue')
        if not datas:
            time.sleep(0.5)
            continue
        datas = json.loads(datas)
        file_name = datas['file_name']
        asr_text = asr_model.inference(file_name)
        if not asr_text:
            datas['msg'] = "ASR result is None"
        else:
            datas['msg'] = 'success'
            datas['asr_text'] = asr_text
        del datas['video_url']
        rpush(rds, 'result_queue', datas)



if __name__ == '__main__':
    # y, sr = librosa.load('/Users/jaho/Jaho/Job/asr_toolkit/pipeline/videos/592f8cbcb46c5d7bc8495c03.mp4')
    # duration = librosa.get_duration(y=y, sr=sr)
    # print(duration)
    asr()
