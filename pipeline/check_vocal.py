import json
import time

from loguru import logger

from api.db import get_redis, rpush
from module.uvr5_model import VocalSeparator
from module.wav_detector import WavDetector
from pipeline.executor_fast_app import Executor

rds = get_redis()


def extract():
    executor = Executor()
    vs = VocalSeparator()
    while True:
        datas = rds.lpop('check_vocal_queue')
        if not datas:
            time.sleep(0.5)
            continue
        datas = json.loads(datas)
        file_name = datas['file_name']
        features = executor.extract_features(file_name)

        filter_result = executor.filter(features)
        if 'Success' not in filter_result:
            datas['msg'] = filter_result
            rpush(rds, 'result_queue', datas)
            continue

        if features['gaps_per_sec'] < 0.1:
            features['asr'] = True
            rpush(rds, 'asr_queue', datas)
        else:
            s, end = (features['duration'] // 2) - 10, (features['duration'] // 2) + 10

            file_path = executor.cut_wav(file_name, s, end)
            # file_path = "dy/" + file
            # 2. 分离人声 background 和 vocal
            try:
                vs.uvr(file_path, agg=15)
            except Exception as e:
                logger.error("分离人声失败: %s" % e)
                datas['msg'] = "分离人声失败"
                rpush(rds, 'result_queue', datas)
                continue
            vocal_path = f"{vs.vocals_path}/{vs.vocal_name}"
            logger.info(file_path)

            try:
                wav_detector = WavDetector()
                vocal_features = wav_detector.extract_features(vocal_path)
            except Exception as e:
                logger.error("wav_detector 失败: %s" % e)
                datas['msg'] = "人声音频特征抽取失败"
                rpush(rds, 'result_queue', datas)
                continue

            features['vocal_db20_splits_size'] = vocal_features['db20_splits_size']
            if vocal_features['db20_splits_size'] < 0.1:
                features['asr'] = True
                rpush(rds, 'asr_queue', datas)
            else:
                features['vocal_qualified'] = False
                features['asr'] = False
                datas['msg'] = "声谱特征排除(db20_splits_size >= 0.1)"
                rpush(rds, 'result_queue', datas)


if __name__ == '__main__':
    extract()
