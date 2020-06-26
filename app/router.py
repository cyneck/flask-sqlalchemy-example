# -*- coding: utf-8 -*-
"""
Create Time: 2020/6/25 23:44
Author: Eric
Desc：路由注册
"""

from app import app
from flask import redirect, render_template, Response

# 导入controller，一个controller对应一个蓝图
from app.controller.home_view import home
from app.controller.commodity_view import commodity

# 注册蓝图 第一个参数 是蓝图对象，第二个参数url前缀
app.register_blueprint(home, url_prefix='/home')
app.register_blueprint(commodity, url_prefix='/commodity')


@app.route('/')
def index():
    return redirect('/home/index')


@app.errorhandler(404)
def page_not_found(e):
    return Response('404', content_type='application/json')


@app.errorhandler(500)
def internal_server_error(e):
    return Response('500', content_type='application/json')
