# -*- coding: utf-8 -*-
"""
Create Time: 2020/6/25 21:13
Author: Eric
Desc：视图控制层
"""

from flask import Blueprint, Response
from flask_cors import CORS

from app import db
from app.model.commodity import Commodity
from app.utils.serialize_util import json_str

commodity = Blueprint("commodity", __name__)
CORS(commodity, supports_credentials=True)


@commodity.route('/index', methods=['GET', 'POST'])
def index():
    page_index = 1
    page_size = 10
    commodity_list = db.session.query(Commodity).filter().offset((int(page_index) - 1) * int(page_size)).limit(
        int(page_size)).all()
    return Response(json_str(commodity_list), content_type='application/json')
