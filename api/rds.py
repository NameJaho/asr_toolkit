import configparser
import json
import os

import redis
from loguru import logger

from tools.utils import get_root_path


def get_redis():
    """创建一个redis链接"""
    config = configparser.ConfigParser()
    config.read(get_root_path() + '/api/config.ini', encoding="utf-8")
    host = config.get('redis', "host")
    port = config.get('redis', "port")
    password = config.get('redis', "password")
    return redis.StrictRedis(host=host, db=2, port=port, password=password)


def rpush(rds,key,datas):
    logger.info(f'{key} +1...')
    rds.rpush(key, json.dumps(datas, ensure_ascii=False))


if __name__ == '__main__':
    rds = get_redis()
    print(rds.llen("test"))
