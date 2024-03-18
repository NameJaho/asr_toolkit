import os
import pandas as pd
import requests

from module.wav_detector import WavDetector


class MyTest(object):
    def __init__(self):
        pass

    @staticmethod
    def load_files():
        files = os.listdir('files')
        return files

    def ts_wav_detector(self):
        files = self.load_files()
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
    def load_tasks():
        df = pd.read_excel('抖音视频文件_v1.2.xlsx')
        return df

    def run_wav_detector(self):
        df = self.load_tasks()
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


if __name__ == '__main__':
    ts = MyTest()
    ts.run_wav_detector()
