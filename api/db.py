import json

import redis
from loguru import logger

from tools.utils import get_root_path
import os
import pandas as pd
from sqlalchemy import create_engine
import configparser


def get_redis():
    """创建一个redis链接"""
    config = configparser.ConfigParser()
    config.read(get_root_path() + '/api/config.ini', encoding="utf-8")
    host = config.get('redis', "host")
    port = config.get('redis', "port")
    password = config.get('redis', "password")
    return redis.StrictRedis(host=host, db=2, port=port, password=password)


def rpush(rds, key, datas):
    logger.info(f'{key} +1...')
    rds.rpush(key, json.dumps(datas, ensure_ascii=False))


class MySQL(object):
    # section 用来选择服务器
    def __init__(self, ini=get_root_path() + '/api/config.ini', section='mysql'):
        self.section = section
        self.config = configparser.ConfigParser()
        self.config.read(ini, encoding="utf-8")
        self.host = self.config.get(section, "host")
        self.password = self.config.get(section, "password")
        self.user = self.config.get(section, "user")
        self.database = self.config.get(section, "database")
        self.port = int(self.config.get(section, "port"))
        self.engine = self.get_connection()

    def get_connection(self):
        user = self.user
        password = self.password
        host = self.host
        port = self.port
        database = self.database
        from urllib.parse import quote_plus as urlquote

        return create_engine(f'mysql+pymysql://{user}:{urlquote(password)}@{host}:{port}/{database}',
                             pool_size=20, max_overflow=50, pool_recycle=30)

    def save(self, ls):
        df = pd.DataFrame(ls)
        print(ls)
        df.drop(columns=['video_url','file_name'], inplace=True)
        df['predictions'] = df['predictions'].apply(lambda x: json.dumps(x, ensure_ascii=False))
        df.to_sql(name='asr', con=self.engine, if_exists='append', index=False)


if __name__ == '__main__':
    # rds = get_redis()
    # print(rds.llen("test"))
    mysql = MySQL()
    ls = [{'video_id': '59355953b46c5d28742493d2', 'label': '家居百货',
           'predictions': [{'label': '母婴用品', 'score': 0.2110194053603136},
                           {'label': '家具', 'score': 0.13405662970311222},
                           {'label': '家居百货', 'score': 0.23352515346102606},
                           {'label': '母婴育儿', 'score': 0.13271365786159606},
                           {'label': '其他', 'score': 0.5592822163222392}],
           'video_url': 'https://sns-video-al.xhscdn.com/lk39Zvs5nFr3PdVOWdbGdpFwHtWd_compress_L1',
           'file_name': 'videos/59355953b46c5d28742493d2.wav', 'msg': '绝对时长小于60s',
           'update_time': '2024-04-02 11:25:47'}, {'video_id': '5934bfb67fc5b87d9b6c3751', 'label': '美妆个护',
                                                   'predictions': [{'label': '美妆个护', 'score': 0.9625673434362627}],
                                                   'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/480x480/vcodec/libx264/pgc/111b2874-3b2e38d-b052-e5a63abe591b?sign=64bf6c4fbf6d63fd6fede8eaa9adb555&t=65fb06d4',
                                                   'msg': '下载失败: 非200响应码',
                                                   'update_time': '2024-04-02 11:25:47'},
          {'video_id': '59340cae14de4141430154fa', 'label': '珠宝配饰',
           'predictions': [{'label': '珠宝配饰', 'score': 0.8736076642199783},
                           {'label': '购物', 'score': 0.2332925922752507}],
           'video_url': 'https://sns-video-al.xhscdn.com/FqAf6l6H_JkP6rswaIaLDxsxlNKZ_compress_L1',
           'file_name': 'videos/59340cae14de4141430154fa.wav', 'msg': '绝对时长小于60s',
           'update_time': '2024-04-02 11:25:47'}, {'video_id': '5932b8f414de410296f5d5cc', 'label': '购物',
                                                   'predictions': [{'label': '音乐', 'score': 0.1317906557233565},
                                                                   {'label': '购物', 'score': 0.16573072848768428},
                                                                   {'label': '其他', 'score': 0.6490792230767078}],
                                                   'video_url': 'https://sns-video-al.xhscdn.com/Fn13xiqbrC0lK0FfI5OcoDVqpNVL_compress_L1',
                                                   'file_name': 'videos/5932b8f414de410296f5d5cc.wav',
                                                   'msg': '绝对时长小于60s', 'update_time': '2024-04-02 11:25:47'},
          {'video_id': '593146607fc5b8385e3260c2', 'label': '购物',
           'predictions': [{'label': '购物', 'score': 0.9878068088951707}],
           'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/3eff0a6f-1ef81dc-bd64-29a04ed418f8?sign=c05f70024abc26047c4291bf014f73d9&t=65fb06d4',
           'msg': '下载失败: 非200响应码', 'update_time': '2024-04-02 11:25:47'},
          {'video_id': '5932b258d2c8a52fede297d2', 'label': '日用百货',
           'predictions': [{'label': '日用百货', 'score': 0.3536088018403554},
                           {'label': '保健品', 'score': 0.157006136064305},
                           {'label': '其他', 'score': 0.6538651087903281}],
           'video_url': 'https://sns-video-al.xhscdn.com/locCwFkWpmVELCTmk70EcOwGgktx_compress_L1',
           'file_name': 'videos/5932b258d2c8a52fede297d2.wav', 'msg': '绝对时长小于60s',
           'update_time': '2024-04-02 11:25:47'}, {'video_id': '592f8cbcb46c5d7bc8495c03', 'label': '宠物用品',
                                                   'predictions': [{'label': '宠物用品', 'score': 0.39370757209911633},
                                                                   {'label': '宠物食品', 'score': 0.22005922807475142},
                                                                   {'label': '零食', 'score': 0.10514209901140233},
                                                                   {'label': '家居百货', 'score': 0.14719804286840057},
                                                                   {'label': '日用百货', 'score': 0.12703011411133022},
                                                                   {'label': '动漫', 'score': 0.23120616233001495},
                                                                   {'label': '宠物', 'score': 0.38945541058508026},
                                                                   {'label': '其他', 'score': 0.27394155976103246}],
                                                   'video_url': 'https://sns-video-al.xhscdn.com/d23df2d0779a89b5301e442ecb3613e3a3d1e8cd_r_ln',
                                                   'file_name': 'videos/592f8cbcb46c5d7bc8495c03.wav',
                                                   'msg': '绝对时长小于60s', 'update_time': '2024-04-02 11:25:47'},
          {'video_id': '592eab22d1d3b97351403be5', 'label': '购物',
           'predictions': [{'label': '购物', 'score': 0.9700028608192598}],
           'video_url': 'https://sns-video-al.xhscdn.com/llSTS9pbw1Tc8xsh6VKNM3fBy8E9_compress_L1',
           'msg': '转换音频失败',
           'update_time': '2024-04-02 11:25:47'}, {'video_id': '592e9db2b46c5d62ce6e4875', 'label': '购物',
                                                   'predictions': [{'label': '美食日常', 'score': 0.13770543654174622},
                                                                   {'label': '时尚穿搭', 'score': 0.22571683885527116},
                                                                   {'label': '购物', 'score': 0.324127312529429},
                                                                   {'label': '其他', 'score': 0.3687757142097227}],
                                                   'video_url': 'https://sns-video-al.xhscdn.com/592e9db2b46c5d62ce6e4875_compress_L1',
                                                   'file_name': 'videos/592e9db2b46c5d62ce6e4875.wav',
                                                   'msg': '绝对时长小于60s', 'update_time': '2024-04-02 11:25:47'},
          {'video_id': '592e6e7b7fc5b83e7a66df03', 'label': '家具',
           'predictions': [{'label': '母婴用品', 'score': 0.2411937249755897},
                           {'label': '家具', 'score': 0.306548268067741},
                           {'label': '家居百货', 'score': 0.18753065490731716},
                           {'label': '家装建材', 'score': 0.28376016635683593},
                           {'label': '其他', 'score': 0.4351295837449095}],
           'video_url': 'https://sns-video-qc.xhscdn.com/encoded/avthumb/mp4/s/853x480/vcodec/libx264/pgc/10fee4ae-5c7c73b-ad4b-24a08fd138c0?sign=d842cdad12236d14fc95b5bcdbd20026&t=65fb06d4',
           'msg': '下载失败: 非200响应码', 'update_time': '2024-04-02 11:25:47'}]
