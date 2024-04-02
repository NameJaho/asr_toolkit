import json
import os
import time

import argparse

import librosa
from loguru import logger

import os
import requests
from threading import Thread
from moviepy.editor import VideoFileClip

from api.db import get_redis, rpush

# 连接到Redis
rds = get_redis()

dirname = 'videos'
if not os.path.exists(dirname):
    os.makedirs(dirname)


def download_video_from_redis():
    while True:
        # 从Redis队列中获取视频URL和ID
        video_data = rds.lpop('classify_queue')
        if video_data is None:
            time.sleep(0.5)
            continue  # 如果队列为空，则继续等待
        datas = json.loads(video_data)
        video_url = datas['video_url']
        id_ = datas['video_id']

        file_name = f'{dirname}/{id_}.mp4'

        try:
            res = requests.get(video_url)
            if res.status_code == 200:
                with open(file_name, 'wb') as f:
                    f.write(res.content)
                try:
                    video_clip = VideoFileClip(file_name)
                    audio_file_name = file_name.rstrip('.mp4') + '.wav'
                    video_clip.audio.write_audiofile(audio_file_name)
                    # 下载成功，将file_name推送到extract_features_queue
                    datas['file_name'] = audio_file_name
                    y, sr = librosa.load(audio_file_name)
                    duration = librosa.get_duration(y=y, sr=sr)
                    if duration < 60:
                        datas['msg'] = "绝对时长小于60s"
                        rpush(rds, 'result_queue', datas)
                        continue

                    db20_splits = librosa.effects.split(y=y, frame_length=4000, top_db=20)
                    db20_splits_size = db20_splits.size / duration
                    if db20_splits_size >= 0.08:
                        rpush(rds, 'asr_queue', datas)
                        continue

                    rpush(rds, 'check_vocal_queue', datas)
                except Exception as e:
                    logger.info(f"转换音频失败: {e}")
                    # 转换失败，也视为整个过程失败
                    datas['msg'] = f'转换音频失败'
                    rpush(rds, 'result_queue', datas)
            else:
                raise Exception("非200响应码")
        except Exception as e:
            logger.info(f"下载失败: {e}")
            # 下载失败，将错误信息推送到result_queue
            datas['msg'] = f'下载失败: {e}'
            rpush(rds, 'result_queue', datas)


def start_downloader_threads(n_threads=2):
    threads = []
    for _ in range(n_threads):
        thread = Thread(target=download_video_from_redis)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == '__main__':
    # 设置命令行参数
    parser = argparse.ArgumentParser(description='从Redis队列下载视频的多线程脚本。')
    parser.add_argument('-t', '--threads', type=int, default=8, help='启动的线程数，默认为4。')
    args = parser.parse_args()

    start_downloader_threads(args.threads)
