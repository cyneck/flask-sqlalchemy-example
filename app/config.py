# -*- coding: utf-8 -*-
"""
Create Time: 2020/6/25 21:21
Author: Eric
Desc：配置
"""

DEBUG = True
CSRF_ENABLED = True
S_PORT = 8080
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@127.0.0.1:3306/ic_kg?charset=utf8'
SECRET_KEY = 'you-will-never-guess'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True
SQLALCHEMY_POOL_SIZE = 5
SQLALCHEMY_POOL_TIMEOUT = 15
