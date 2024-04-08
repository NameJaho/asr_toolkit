import json

import redis
from loguru import logger

from tools.utils import get_root_path
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
        # print(ls)
        if 'video_url' in df.columns:
            df.drop(columns=['video_url'], inplace=True)
        if 'file_name' in df.columns:
            df.drop(columns=['file_name'], inplace=True)
        df['predictions'] = df['predictions'].apply(lambda x: json.dumps(x, ensure_ascii=False))
        for _ in range(3):
            try:
                df.to_sql(name='asr', con=self.engine, if_exists='append', index=False)
                break
            except Exception as e:
                logger.error(f"save to mysql error: {e}")
                self.engine = self.get_connection()
        # df.to_sql(name='asr', con=self.engine, if_exists='append', index=False)

    def get_data(self, start_time, end_time):
        if not start_time:
            sql = "select * from asr order by update_time desc"
        else:
            sql = f"select * from asr where update_time>='{start_time}' and update_time <'{end_time}' order by update_time desc"
        df = pd.read_sql_query(sql, self.engine)
        df['update_time'] = df['update_time'].apply(lambda x: x.strftime('%Y-%m-%d %H:%M:%S'))
        dict_result = df.to_dict(orient='records')
        return json.dumps(dict_result, ensure_ascii=False)


if __name__ == '__main__':
    # rds = get_redis()
    # print(rds.llen("test"))
    mysql = MySQL()
    print(mysql.get_data())
