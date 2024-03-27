import os
import re
import time

import pandas as pd
import requests
from moviepy.video.io.VideoFileClip import VideoFileClip

from module.asr_model import ASRModel
from module.wav_detector import WavDetector
from pydub import AudioSegment
from module.uvr5_model import VocalSeparator
from tools.utils import get_root_path
from loguru import logger


class MyTest(object):
    def __init__(self):
        self.asr_model = ASRModel()

    @staticmethod
    def load_files(dir_name):
        files = [i for i in os.listdir(dir_name) if 'wav' in i]
        return files

    def ts_wav_detector(self):
        files = self.load_files('files')
        result = []
        for file in files:
            if not file.endswith('wav'):
                continue
            wav_detector = WavDetector('files/' + file)

            features = wav_detector.extract_features()
            features['file'] = file
            result.append(features)
        df = pd.DataFrame(result)
        df.to_excel('result.xlsx', index=False)

    @staticmethod
    def load_tasks(name):
        # df = pd.read_excel('小红书视频文件_v1.2.xlsx')
        # df = pd.read_excel('抖音视频文件_v1.2.xlsx')
        df = pd.read_excel(name)
        return df

    def run_wav_detector(self):
        df = self.load_tasks('240321_小红书视频文章随机3000篇.xlsx')
        result_ls = []
        for index, row in df.iterrows():
            if pd.isna(row['title']):
                continue
            if not os.path.exists('dy/' + str(row['id']) + '.mp4'):
                res = requests.get(row['file_path'])
                with open('dy/' + str(row['id']) + '.mp4', 'wb') as f:
                    f.write(res.content)
            try:

                wav_detector = WavDetector('dy/' + str(row['id']) + '.mp4')
                features = wav_detector.extract_features()

            except:
                print('dy/' + str(row['id']) + '==> error')
                continue

            features['title'] = row['title']
            features['id'] = row['id']
            features['video_tag_list'] = row['video_tag_list']
            features['file_path'] = row['file_path']
            result_ls.append(features)
        result_df = pd.DataFrame(result_ls)
        result_df.to_excel('result_dy2.xlsx', index=False)

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

    def download_and_load(self, name, dirname='dy'):
        if not os.path.exists(dirname):
            os.makedirs(dirname)

        df = self.load_tasks(name)
        for index, row in df.iterrows():
            if pd.isna(row['title']):
                continue
            if not os.path.exists(f'{dirname}/' + str(row['id']) + '.mp4'):
                try:
                    res = requests.get(row['video_url'])
                except:
                    continue
                with open(f'{dirname}/' + str(row['id']) + '.mp4', 'wb') as f:
                    f.write(res.content)
                try:

                    video_clip = VideoFileClip(f'{dirname}/' + str(row['id']) + '.mp4')
                    video_clip.audio.write_audiofile(f'{dirname}/' + str(row['id']) + '.wav')
                except:
                    continue
        files = self.load_files(f'{dirname}')
        return files

    def ts_cut_wav(self):
        files = self.load_files('files')  # 读取本地文件
        # files = self.download_and_load()  # 下载文件并读取
        result = []
        vs = VocalSeparator()
        print(files)
        # 1. 将音频文件切割成10s
        for index, file in enumerate(files):
            # if index < 50:
            #     continue
            if not file.endswith('wav'):
                continue
            file_path = self.cut_wav('files/' + file)
            # 2. 分离人声 background 和 vocal
            try:
                vs.uvr(file_path, agg=15)
            except:
                continue
            background_path = f"{vs.background_path}/{vs.background_name}"
            vocal_path = f"{vs.vocals_path}/{vs.vocal_name}"
            print(file_path)

            # 3. 分别提取特征
            for path in [background_path, vocal_path]:
                try:
                    wav_detector = WavDetector(path)
                    features = wav_detector.extract_features()
                except:
                    continue
                features['file'] = file
                features['type'] = 'vocals' if 'vocals' in path else 'background'
                result.append(features)

        df = pd.DataFrame(result)
        df.to_excel('result_02.xlsx', index=False)


    def process(self):
        # excel = '240321_小红书视频文章随机3000篇.xlsx'
        excel = 'result.xlsx'
        dirname = 'xhs3000'
        df = self.load_tasks(excel)

        vs = VocalSeparator()
        files = self.download_and_load(excel, dirname=dirname)  # 下载文件并读取

        result = []
        for index, file in enumerate(files):
            # if index <= 500:
            #     continue
            print(file)
            filename = re.findall('(.*?).wav', file)[0]

            if not file.endswith('wav'):
                continue
            try:
                wav_detector = WavDetector(f'{dirname}/' + file)
                features = wav_detector.extract_features()
            except:
                continue
            if self.filter(features):
                if features['db20_splits_size'] >= 0.08:
                    features['music_detected'] = False
                    features['asr'] = True
                else:
                    features['music_detected'] = True
                    if features['gaps_per_sec'] < 0.1:
                        features['asr'] = True
                        continue

                    s, end = (features['duration'] // 2) - 10, (features['duration'] // 2) + 10

                    file_path = self.cut_wav(f'{dirname}/' + file, s, end)
                    # file_path = "dy/" + file
                    # 2. 分离人声 background 和 vocal
                    try:
                        vs.uvr(file_path, agg=15)
                    except Exception as e:
                        logger.error("分离人声失败: %s" % e)
                        continue
                    vocal_path = f"{vs.vocals_path}/{vs.vocal_name}"
                    logger.info(file_path)

                    try:
                        wav_detector = WavDetector(vocal_path)
                        vocal_features = wav_detector.extract_features()
                    except Exception as e:
                        logger.error("wav_detector失败: %s" % e)
                        continue
                    features['vocal_db20_splits_size'] = vocal_features['db20_splits_size']
                    if vocal_features['db20_splits_size'] < 0.1:
                        features['vocal_qualified'] = True
                        features['asr'] = True
                    else:
                        features['vocal_qualified'] = False
                        features['asr'] = False
            else:
                continue
            features['id'] = filename
            features['name'] = df.loc[df['id'] == int(filename), 'title'].values[0]
            features['video_url'] = df.loc[df['id'] == int(filename), 'video_url'].values[0]
            features['tag_list'] = df.loc[df['id'] == int(filename), 'tag_list'].values[0]
            features['asr_text'] = self.asr_model.inference(f'{dirname}/' + file)
            result.append(features)

        df = pd.DataFrame(result)
        df.to_excel(f'process_{dirname}.xlsx', index=False)

    def process_v2(self):
        """
            不检测 music_detected
        """
        df = self.load_tasks()

        vs = VocalSeparator()
        files = self.download_and_load()  # 下载文件并读取

        result = []
        for index, file in enumerate(files):

            print(file)
            filename = re.findall('(.*?).wav', file)[0]

            if not file.endswith('wav'):
                continue
            try:
                wav_detector = WavDetector("dy/" + file)
                features = wav_detector.extract_features()
            except:
                continue
            if self.filter(features):

                s, end = (features['duration'] // 2) - 10, (features['duration'] // 2) + 10

                file_path = self.cut_wav('dy/' + file, s, end)
                # file_path = "dy/" + file
                # 2. 分离人声 background 和 vocal
                try:
                    vs.uvr(file_path, agg=15)
                except Exception as e:
                    logger.error("分离人声失败: %s" % e)
                    continue
                vocal_path = f"{vs.vocals_path}/{vs.vocal_name}"
                print(file_path)

                try:
                    wav_detector = WavDetector(vocal_path)
                    vocal_features = wav_detector.extract_features()
                except Exception as e:
                    logger.error("wav_detector失败: %s" % e)
                    continue
                features['vocal_db20_splits_size'] = vocal_features['db20_splits_size']
                if vocal_features['db20_splits_size'] < 0.1:
                    features['vocal_qualified'] = True
                    features['asr'] = True
                else:
                    features['vocal_qualified'] = False
                    features['asr'] = False

            features['id'] = filename
            features['name'] = df.loc[df['id'] == int(filename), 'title'].values[0]
            features['file_path'] = df.loc[df['id'] == int(filename), 'file_path'].values[0]
            features['video_tag_list'] = df.loc[df['id'] == int(filename), 'video_tag_list'].values[0]
            result.append(features)

        df = pd.DataFrame(result)
        df.to_excel('process_without_cut_03.xlsx', index=False)

    @staticmethod
    def filter(features):
        if features['duration'] > 30 and features['vocal_pct'] > 0.7 and features['vocal_duration'] > 30000:
            print(f'features is ok : {features}')
            return True
        return False

    def tmp(self):
        import librosa
        import matplotlib.pyplot as plt
        import numpy as np
        audio_path = '/Users/jaho/Jaho/Job/asr_toolkit/output/vocals/vocal_482.wav_15.wav'
        # wav_detector = WavDetector('/Users/jaho/Jaho/Job/asr_toolkit/output/vocals/vocal_452.wav_15.wav')
        # vocal_features = wav_detector.extract_features()
        # # 加载音频文件
        y, sr = librosa.load(audio_path)

        # 计算声谱图
        S = librosa.feature.melspectrogram(y=y, sr=sr)
        S_DB = librosa.power_to_db(S, ref=np.max)
        # 绘制声谱图
        plt.figure(figsize=(10, 4))
        librosa.display.specshow(S_DB, sr=sr, x_axis='time', y_axis='mel')
        plt.colorbar(format='%+2.0f dB')
        plt.title('Mel-frequency spectrogram')
        plt.tight_layout()
        plt.show()

        # print(vocal_features)


if __name__ == '__main__':
    ts = MyTest()
    start = time.time()
    # ts.run_wav_detector()
    # ts.ts_cut_wav()
    # ts.process()
    import requests

    data = {
        "video_url": "https://sns-video-hw.xhscdn.net/2_5821beb8b46c5d0e371d7f11_compress_L1",
        "video_id": "2_5821beb8b46c5d0e371d7f11_compress_L1"
    }
    res = requests.post('http://127.0.0.1:23002/video/parse', json=data)
    print(res.json())
    print(time.time() - start)
    # ts.tmp()
