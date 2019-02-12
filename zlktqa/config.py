import os

DEBUG = True

SECRET_KEY = os.urandom(24)

HOST_NAME = '127.0.0.1'
PORT      = '3306'
DATABASE  = 'zlktqa_demo'
USERNAME  = 'root'
PASSWORD  = 'root'
DB_URI = 'mysql+mysqldb://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOST_NAME,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI