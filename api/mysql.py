import os
import re
import pandas as pd
from sqlalchemy import create_engine
import configparser

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class MySQL(object):
    # section 用来选择服务器
    def __init__(self, ini=os.path.join(BASE_DIR, '../config/config.ini'), section='datayes'):
        self.section = section
        self.config = configparser.ConfigParser()
        self.config.read(ini, encoding="utf-8")
        self.host = self.config.get(section, "host")
        self.password = self.config.get(section, "password")
        self.user = self.config.get(section, "user")
        self.database = self.config.get(section, "database")
        self.port = int(self.config.get(section, "port"))

    def get_connection(self):
        user = self.user
        password = self.password
        host = self.host
        port = self.port
        database = self.database
        from urllib.parse import quote_plus as urlquote

        return create_engine(f'mysql+pymysql://{user}:{urlquote(password)}@{host}:{port}/{database}',
                             pool_size=20, max_overflow=50, pool_recycle=30)

    def run_sql(self, sql):
        engine = self.get_connection()
        df = pd.read_sql_query(sql, engine)
        return df

if __name__ == '__main__':
    mysql = MySQL()
    result = mysql.run_sql("show tables;")
    print(result)
