import json
import re

import pandas as pd
import requests
from fastapi import FastAPI
from moviepy.video.io.VideoFileClip import VideoFileClip
from numpy import float32
from pydub import AudioSegment

from api.db import get_redis, MySQL
from api.request import MainRequest, ClsRequest, BatchRequest, GetDataRequest
from api.response import TargetCatResponseData, MainResponseData, ClsResponseData
from module.classify_api import classify, batch_classify
from module.wav_detector import WavDetector
from tools import audio_extractor
from module.uvr5_model import VocalSeparator
from tools.utils import *
from loguru import logger
from tools.utils import timer
import os

INPUT_VIDEOS_FOLDER = 'data'
OUTPUT_AUDIOS_FOLDER = 'output/audios'
OUTPUT_TEXTS_FOLDER = 'output/texts'

app = FastAPI(title='Asr System', version='1.0.0',
              )


def get_response(data: dict = None, code=200):
    """
    统一响应
    """
    return data


class Executor:
    def __init__(self):
        self.vocal_separator = VocalSeparator()
        # self.asr_model = ASRModel()
        # self.vs = VocalSeparator()
        self.wav_detector = WavDetector()

        self.target_category = ["宠物用品", "宠物食品", "零食", "母婴用品", "家具", "家居百货", "珠宝配饰", "日用百货",
                                "食品饮料", "电器", "保健品", "科技数码", "美妆个护", "购物", ]
        self.rds = get_redis()

    @staticmethod
    @timer
    def convert_videos(input_folder=INPUT_VIDEOS_FOLDER):
        input_paths = get_file_paths(input_folder)

        if not os.path.exists(OUTPUT_AUDIOS_FOLDER):
            os.makedirs(OUTPUT_AUDIOS_FOLDER)

        logger.info('Videos to audios conversion started...')
        for input_folder in input_paths:
            input_file_name = get_file_name(input_folder)
            output_file_name = f'{input_file_name}.wav'
            output_file_path = os.path.join(OUTPUT_AUDIOS_FOLDER, output_file_name)

            if not os.path.exists(output_file_path):
                audio_extractor.extract_audio(input_folder, output_file_path)
        logger.info('Videos to audios conversion completed...')

    @timer
    def separate_vocals(self):
        logger.info('Vocals separation started...')
        self.vocal_separator.uvr()
        logger.info('Vocals separation completed...')

    @timer
    def asr(self, input_folder=OUTPUT_AUDIOS_FOLDER, output_folder=OUTPUT_TEXTS_FOLDER):
        input_paths = get_file_paths(input_folder)

        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        logger.info('ASR started...')

        for input_path in input_paths:
            input_file_name = get_file_name(input_path)
            output_file_name = f'{input_file_name}.txt'
            output_file_path = os.path.join(output_folder, output_file_name)

            if not os.path.exists(output_file_path):
                text = self.asr_model.inference(input_path)
                write_text_to_file(text, output_file_path)
        logger.info('ASR completed...')

    @staticmethod
    def download(video_url, id_):
        dirname = 'videos'
        if not os.path.exists(dirname):
            os.makedirs(dirname)
        # id_ = re.findall('guoc_test_(.*)', video_url)[0]
        file_name = f'{dirname}/' + str(id_) + '.mp4'
        if not os.path.exists(file_name):
            try:
                res = requests.get(video_url)
            except:
                return False
            with open(file_name, 'wb') as f:
                f.write(res.content)
            try:
                video_clip = VideoFileClip(file_name)
                video_clip.audio.write_audiofile(file_name.rstrip('.mp4') + '.wav')
            except:
                return "下载失败"
        return file_name

    def extract_features(self, file_name):
        try:
            features = self.wav_detector.extract_features(file_name)
        except:
            import traceback
            logger.error(traceback.format_exc())
            return {}
        else:
            return features

    @staticmethod
    def filter(features):
        if features['duration'] <= 60:
            return "绝对时长小于60s"
        if features['vocal_pct'] <= 0.7:
            return "人声占比小于0.7"
        if features['vocal_duration'] <= 30000:
            return "人声时长小于30s"

        print(f'features is ok : {features}')
        return "Success"

    @staticmethod
    def cut_wav(file_path, start_time, end_time):
        filename = re.findall('.*/(.*?.wav)', file_path)[0]
        # 加载音频文件
        audio = AudioSegment.from_wav(file_path)

        # 定义开始和结束时间（毫秒）
        # start_time = 10000  # 从10秒开始
        # end_time = 20000  # 到20秒结束

        # 截短音频
        shortened_audio = audio[start_time * 1000:end_time * 1000]
        if not os.path.exists(get_root_path() + '/output/cut'):
            os.makedirs(get_root_path() + '/output/cut')
        # 导出截短后的音频
        shortened_audio.export(get_root_path() + '/output/cut/' + filename, format="wav")
        return get_root_path() + '/output/cut/' + filename

    @staticmethod
    def format_feature(data):
        for k, v in data.items():
            if isinstance(v, float32):
                data[k] = round(float(v), 2)
        return data

    @staticmethod
    def classify(content1, title):
        if len(content1) > 100:
            content = title + re.findall('.*?(#.*)', content1)[0] if '#' in content1 else title
        else:
            content = title + content1
        if content:
            content = re.sub('\?|❗|？', ',', content)
            content = re.sub('\[话题\]', ' ', content)
        else:
            content = content1
        label, predictions = classify(content)
        if not label and not predictions:
            return "分类失败", "分类失败"
        return label, predictions

    @staticmethod
    def pre_classify(tasks):
        ls = []

        for title, content1 in tasks:
            if len(content1) > 100:
                content = title + re.findall('.*?(#.*)', content1)[0] if '#' in content1 else title
            else:
                content = title + content1
            if content:
                content = re.sub('\?|❗|？', ',', content)
                content = re.sub('\[话题\]', ' ', content)
            else:
                content = content1
            ls.append(content)
        return ls

    def process(self, video_url, video_id, video_tag_list, title, content):
        base_resp = {
            "predictions": [],
            "label": "",
            "asr_text": "",
            'msg': '',
            'video_id': video_id,
            'code': -1
        }
        result = self.classify(content, title)
        if result == "分类失败":
            base_resp['msg'] = "分类失败"
            return base_resp
        label, predictions = result
        if label not in self.target_category:
            base_resp['msg'] = "不在目标分类中"
            base_resp['label'] = label
            base_resp['predictions'] = predictions
            return base_resp

        file_name = self.download(video_url, video_id)
        if not file_name:
            base_resp['msg'] = "视频下载失败"
            base_resp['label'] = label
            base_resp['predictions'] = predictions
            return "视频下载失败"

        features = self.extract_features(file_name)
        if not features:
            base_resp['msg'] = "特征抽取失败"
            base_resp['label'] = label
            base_resp['predictions'] = predictions
            return base_resp

        filter_result = self.filter(features)

        if 'Success' not in filter_result:
            base_resp['msg'] = filter_result
            base_resp['label'] = label
            base_resp['predictions'] = predictions
            return base_resp

        if features['db20_splits_size'] >= 0.08:
            features['music_detected'] = False
            features['asr'] = True

        else:
            features['music_detected'] = True
            if features['gaps_per_sec'] < 0.1:
                features['asr'] = True
            else:
                s, end = (features['duration'] // 2) - 10, (features['duration'] // 2) + 10

                file_path = self.cut_wav(file_name, s, end)
                # file_path = "dy/" + file
                # 2. 分离人声 background 和 vocal
                try:
                    self.vs.uvr(file_path, agg=15)
                except Exception as e:
                    logger.error("分离人声失败: %s" % e)
                    return "分离人声失败"
                vocal_path = f"{self.vs.vocals_path}/{self.vs.vocal_name}"
                logger.info(file_path)

                try:
                    wav_detector = WavDetector()
                    vocal_features = wav_detector.extract_features(vocal_path)
                except Exception as e:
                    logger.error("wav_detector 失败: %s" % e)

                    base_resp['msg'] = "人声音频特征抽取失败"
                    base_resp['label'] = label
                    base_resp['predictions'] = predictions
                    return base_resp

                features['vocal_db20_splits_size'] = vocal_features['db20_splits_size']
                if vocal_features['db20_splits_size'] < 0.1:
                    features['vocal_qualified'] = True
                    features['asr'] = True
                else:
                    features['vocal_qualified'] = False
                    features['asr'] = False

                    base_resp['msg'] = "声谱特征排除(db20_splits_size >= 0.1)"
                    base_resp['label'] = label
                    base_resp['predictions'] = predictions
                    return base_resp
        features['id'] = video_id
        features['title'] = title
        features['label'] = label
        features['predictions'] = predictions
        features['video_tag_list'] = video_tag_list
        features['video_url'] = video_url
        features['asr_text'] = self.asr_model.inference(file_name)[0]['text']
        result = {
            "predictions": predictions,
            "label": label,
            'asr_text': features['asr_text'],
        }

        base_resp['msg'] = "success"
        base_resp['label'] = label
        base_resp['predictions'] = predictions
        base_resp['asr_text'] = features['asr_text']
        # return self.format_feature(features)
        return base_resp

    @timer
    def batch_classify(self, datas):
        df = pd.DataFrame(datas)
        base_resp = {
            "predictions": [],
            "label": "",
            "asr_text": "",
            'msg': '',
            'video_id': "",
            'code': -1
        }
        tasks = self.pre_classify(
            [[i['title'], i['content']] for i in df[['title', 'content']].to_dict(orient='records')])
        label_result = batch_classify(tasks)
        df['predictions'] = [item['predictions'] for item in label_result]
        df['label'] = [item['label'] for item in label_result]
        df['target'] = df['label'].apply(lambda x: "不在目标分类中" if x not in self.target_category else "")
        target = df[df['target'] == ''][['video_id', 'label', 'predictions', 'video_url']]
        self.save_to_redis('classify_queue', target.to_dict(orient='records'))
        return f'classify_queue 新增{target.__len__()}条数据'

    def save_to_redis(self, name, values):
        [self.rds.lpush(name, json.dumps(i, ensure_ascii=False)) for i in values]


executor = Executor()


@app.post(path="/video/parse", response_model=MainResponseData, summary="统一入口")
def execute(request: MainRequest):
    video_url = request.video_url
    video_id = request.video_id
    video_tag_list = request.video_tag_list
    title = request.title
    content = request.content
    logger.info(video_url)
    # executor = Executor()
    features = executor.process(video_url, video_id, video_tag_list, title, content)
    logger.info(features)
    return get_response(features)


@app.post(path="/batch", summary="批量处理视频1")
def batch(request: BatchRequest):
    datas = request.data
    msg = executor.batch_classify(datas)
    logger.info(msg)
    return msg


@app.post(path="/get_datas", summary="获取数据")
def get_data(request: GetDataRequest):
    update_time = request.update_time
    mysql = MySQL()
    datas = mysql.get_data(update_time)
    return datas


@app.post(path="/target_categories", response_model=TargetCatResponseData, summary="获取目标分类")
def get_categories():
    # executor = Executor()
    return get_response({
        'categories': executor.target_category,
        'msg': 'success',
        'code': 200

    })


@app.post(path="/classify", response_model=ClsResponseData, summary="传入content和title进行分类")
def classify_(request: ClsRequest):
    # executor = Executor()
    content = request.content
    title = request.title
    label, predictions = executor.classify(content, title)
    return get_response({
        'label': label,
        'predictions': predictions,
        'msg': 'success',
        'code': 200
    })


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("executor_fast_app:app", host="0.0.0.0", port=8899, reload=True)
    # uvicorn.run(app, host="0.0.0.0", port=7879)

# 1000条数据 3s-4s
# 1. 批量（1000条）传入content,title调用接口分类，返回符合条件的视频id等信息 进入classify_queue(video_id,label,predictions) 失败进入 result_queue (video_id,label,predictions,msg)

# 多线程下载
# 2. classify_queue:下载符合条件的视频，转音频 根据音频绝对时长、db20_splits_size 进行初步筛选  classify_queue(video_id,label,predictions) 失败进入 result_queue (video_id,label,predictions,msg)
# db20_splits_size小于0.08进入extract_features_queue 大于进入 asr_queue

# 单线程处理
# 3. extract_features_queue: check_vocal，筛选音频时长、人声占比、人声时长等  成功进入asr_queue(video_id,label,predictions)  失败进入 result_queue (video_id,label,predictions,msg)

# 可多线程处理
# 4. asr_queue:进行asr识别  结果存入 result_queue (video_id,label,predictions,msg)

# 5. pop result_queue to mysql
