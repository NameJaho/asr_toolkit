import argparse
import json
import time
from threading import Thread

import librosa

from api.db import get_redis, rpush
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
        for _ in range(3):
            try:
                asr_text = asr_model.inference(file_name)
                break
            except Exception as e:
                asr_text = f"asr error:{str(e)}"
                time.sleep(1)
        if not asr_text:
            datas['msg'] = "ASR result is None"
        elif 'error' in asr_text:
            datas['msg'] = asr_text
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
