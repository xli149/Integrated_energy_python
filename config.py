import os
from datetime import timedelta

basedir = os.path.abspath(os.path.dirname(__name__))


# 创建应用app的基础配置类
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'this is hard secret_key'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SEND_FILE_MAX_AGE_DEFAULT = timedelta(seconds=1)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test.db')

