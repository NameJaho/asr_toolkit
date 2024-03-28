import re
import requests
from fastapi import FastAPI
from moviepy.video.io.VideoFileClip import VideoFileClip
from numpy import float32
from pydub import AudioSegment

from api.request import MainRequest, ClsRequest
from api.response import MainResponse, TargetCatResponseData, ClsResponse
from module.classify_api import classify
from module.wav_detector import WavDetector
from tools import audio_extractor
from module.uvr5_model import VocalSeparator
from module.asr_model import ASRModel
from tools.utils import *
from loguru import logger
from tools.utils import timer
import os

# app = Flask(__name__)

INPUT_VIDEOS_FOLDER = 'data'
OUTPUT_AUDIOS_FOLDER = 'output/audios'
OUTPUT_TEXTS_FOLDER = 'output/texts'

app = FastAPI(title='Asr System', version='1.0.0',
              )


# app.add_exception_handler(CategoryError, category_error_handler)


def get_response(data: dict = None, code=200):
    """
    统一响应
    """
    return {
        "code": code,
        "data": data
    }


class Executor:
    def __init__(self):
        self.vocal_separator = VocalSeparator()
        self.asr_model = ASRModel()
        self.vs = VocalSeparator()
        self.target_category = ["宠物用品", "宠物食品", "零食", "母婴用品", "家具", "家居百货", "珠宝配饰", "日用百货",
                                "食品饮料", "电器", "保健品", "科技数码", "美妆个护", "购物", ]

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
                return False
        return file_name

    @staticmethod
    def extract_features(file_name):
        try:
            wav_detector = WavDetector(file_name)
            features = wav_detector.extract_features()
        except:
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
                data[k] = float(v)
        return data

    @staticmethod
    def classify(content, title):
        if len(content) > 100:
            content = title + re.findall('.*?(#.*)', content)[0] if '#' in content else title
        else:
            content = title + content
        if content:
            content = re.sub('\?|❗|？', ',', content)
            content = re.sub('\[话题\]', ' ', content)
        label, predictions = classify(content)
        if not label and not predictions:
            return "分类失败"
        return label, predictions

    def process(self, video_url, video_id, video_tag_list, title, content):
        result = self.classify(content, title)
        if result == "分类失败":
            return result
        label, predictions = result
        if label not in self.target_category:
            return "不在目标分类中"

        file_name = self.download(video_url, video_id)
        if not file_name:
            return "视频下载失败"

        features = self.extract_features(file_name)
        if not features:
            return "特征抽取失败"

        filter_result = self.filter(features)

        if 'Success' not in filter_result:
            return filter_result

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
                    wav_detector = WavDetector(vocal_path)
                    vocal_features = wav_detector.extract_features()
                except Exception as e:
                    logger.error("wav_detector 失败: %s" % e)
                    return "人声音频特征抽取失败"

                features['vocal_db20_splits_size'] = vocal_features['db20_splits_size']
                if vocal_features['db20_splits_size'] < 0.1:
                    features['vocal_qualified'] = True
                    features['asr'] = True
                else:
                    features['vocal_qualified'] = False
                    features['asr'] = False
                    return "声谱特征排除(db20_splits_size >= 0.1)"
        features['id'] = video_id
        features['title'] = title
        features['label'] = label
        features['predictions'] = predictions
        features['video_tag_list'] = video_tag_list
        features['video_url'] = video_url
        features['asr_text'] = self.asr_model.inference(file_name)[0]['text']
        return self.format_feature(features)


@app.post(path="/video/parse", response_model=MainResponse, summary="统一入口")
def execute(request: MainRequest):
    video_url = request.video_url
    video_id = request.video_id
    video_tag_list = request.video_tag_list
    title = request.title
    content = request.content
    logger.info(video_url)
    executor = Executor()
    features = executor.process(video_url, video_id, video_tag_list, title, content)
    logger.info(features)
    if isinstance(features, str):
        return get_response({
            "code": -1,
            "msg": features,
        })
    else:
        return get_response({
            'features': features,
            'msg':'success'
        })


@app.post(path="/target_categories", response_model=TargetCatResponseData, summary="获取目标分类")
def get_categories():
    executor = Executor()
    return get_response({
        'data': executor.target_category,
        'msg': 'success'

    })


@app.post(path="/classify", response_model=ClsResponse, summary="传入content和title进行分类")
def classify_(request: ClsRequest):
    executor = Executor()
    content = request.content
    title = request.title
    label, predictions = executor.classify(content, title)
    return get_response({
        'label': label,
        'predictions': predictions,
        'msg': 'success'

    })


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("executor_fast_app:app", host="0.0.0.0", port=8899, reload=True)
    # uvicorn.run(app, host="0.0.0.0", port=7879)
# curl -X POST -H "Content-Type: application/json" -d '{"video_url": "guoc_test_00006afed434d4eb95af94b1ef03dac2"}' http://127.0.0.1:23002/video/parse
