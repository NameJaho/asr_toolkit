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
    # asr()
    ls = [
        'videos/58a1d666d1d3b908bf7fa0b6.wav',
        'videos/58a2d2d57836236d558255ac.wav',
        'videos/58a110a7b46c5d61f5da5a77.wav',
        'videos/58a179c8b46c5d5044edddd3.wav',
        'videos/58aa85f4b46c5d45275e62f8.wav',
        'videos/58aafecffaa05253bf785562.wav',
        'videos/58aead20d5945f385c9b5b66.wav',
        'videos/58afecaa346094518188bb6a.wav',
        'videos/58b8e44bfaa0527ad081c95a.wav',
        'videos/58b3970dd2c8a548eea0b6cd.wav',
    ]
    lens = 0
    s = time.time()
    for i in ls:
        asr_text = asr_model.inference(i)
        lens += len(asr_text)
        print(lens)
    print(time.time() - s)
