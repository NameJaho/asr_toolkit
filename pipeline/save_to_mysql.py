import json
import os
import time
import requests

from loguru import logger

from api.db import MySQL, get_redis
from tools.utils import get_root_path


def saving():
    mysql = MySQL()
    rds = get_redis()
    chunk = []
    success_cnt = 0
    start = int(time.time())
    while True:
        # 从Redis队列中获取视频URL和ID
        video_data = rds.lpop('result_queue')
        if not video_data:
            time.sleep(0.1)
            continue
        datas = json.loads(video_data)
        datas['update_time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if datas.get('msg') == 'success':
            success_cnt += 1
        chunk.append(datas)
        # delete video file by video_id
        # os.system(f"rm -rf {root_path}/videos/{datas['video_id']}.mp4")
        # os.system(f"rm -rf {root_path}/videos/{datas['video_id']}.wav")
        # time.sleep(0.5)

        # logger.info(f"delete {root_path}/videos/{datas['video_id']}")
        if len(chunk) < 1000 or time.time() - start < 300:
            continue
        else:
            logger.info(f"save {chunk.__len__()} datas to mysql")
            send(f"save {chunk.__len__()} datas to mysql success_cnt: {success_cnt}")
            mysql.save(chunk)
            delete_videos(chunk)
            chunk.clear()
            start = time.time()
            success_cnt = 0


def delete_videos(chunk):
    root_path = get_root_path()

    for item in chunk:
        filename = f"{root_path}/videos/{item['video_id']}.mp4"
        # 判断文件是否存在
        if os.path.exists(filename):
            # 如果文件存在，删除文件
            os.remove(filename)
            time.sleep(0.1)
            os.remove(filename.replace('mp4', 'wav'))
            logger.info(f"文件 '{filename}' 已删除")
        else:
            logger.info(f"文件 '{filename}' 不存在")


def send(message):
    # aite的相关人手机号
    mentioned_mobile_list = [15088132627, 18538775625]
    qun_id = '2bc81e07-3ed6-4ccc-8cd0-81a601f1aca6'
    request = {"url": 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={}'.format(qun_id),
               "headers": {"Content-Type": "application/json"},
               "json": {"msgtype": "text", "text": {"content": message}}
               }
    rs = requests.post(**request)


if __name__ == '__main__':
    saving()
