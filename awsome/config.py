import os

DEBUG = True

SECRET_KEY = os.urandom(24)

HOST_NAME = '127.0.0.1'
PORT      = '3306'
DATABASE  = 'ktqa_demo'
USERNAME  = 'root'
PASSWORD  = 'root'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOST_NAME,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI

#跟踪SQLALCHEMY发生的修改
SQLALCHEMY_TRACK_MODIFICATIONS = False
