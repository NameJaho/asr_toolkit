import json
import time

from loguru import logger

from api.db import MySQL, get_redis


def saving():
    mysql = MySQL()
    rds = get_redis()
    chunk = []
    start = int(time.time())
    while True:
        # 从Redis队列中获取视频URL和ID
        video_data = rds.lpop('result_queue')
        if not video_data:
            time.sleep(0.1)
            continue
        datas = json.loads(video_data)
        datas['update_time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        chunk.append(datas)
        if len(chunk) < 1000 and time.time() - start < 600:
            continue
        else:
            mysql.save(chunk)
            chunk.clear()
            logger.info(f"save data to mysql")
            start = time.time()


if __name__ == '__main__':
    saving()
