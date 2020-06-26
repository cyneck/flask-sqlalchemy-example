# -*- coding: utf-8 -*-
"""
Create Time: 2020/6/25 21:24
Author: Eric
Desc：app下全局初始化共享对象
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)

# 导入router.py文件,放在db初始化后面
from app import router
