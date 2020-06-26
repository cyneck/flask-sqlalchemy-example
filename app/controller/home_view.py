# -*- coding: utf-8 -*-
"""
Create Time: 2020/6/25 23:51
Author: Eric
Desc：首页
"""

from flask import Blueprint, render_template

#  创建蓝图 第一个参数为蓝图的名字
home = Blueprint('home', __name__)


@home.route('/index')
def index():
    return render_template('home/index.html')
