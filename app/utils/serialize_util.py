# -*- coding: utf-8 -*-
"""
Create Time: 2020/6/25 22:16
Author: Eric
Desc：Todo
"""
import hashlib
import json

from flask import jsonify
from sqlalchemy.ext.declarative import DeclarativeMeta


class AlchemyJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj) if hasattr(obj, x) and not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
                try:
                    json.dumps(data)  # this will fail on non-encodable values, like other classes
                    fields[field] = data
                except TypeError:
                    # fields[field] = None
                    pass
            # a json-encodable dict
            return fields

        return json.JSONEncoder.default(self, obj)


# 序列化对象
def serialize_model(model):
    from sqlalchemy.orm import class_mapper
    columns = [c.key for c in class_mapper(model.__class__).columns]
    return dict((c, getattr(model, c)) for c in columns)


def json_str(data):
    return json.dumps(data, ensure_ascii=True, cls=AlchemyJsonEncoder).replace(u'\xa0', u'')


def json_str2(data):
    return jsonify(data)


# md5加密
def str_to_md5(text):
    m = hashlib.md5()
    m.update(text.encode("utf8"))
    return m.hexdigest()
