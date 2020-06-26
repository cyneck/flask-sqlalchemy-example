# -*- coding: utf-8 -*-
"""
Create Time: 2020/6/21 11:26
Author: Eric
Desc：Commodity
"""
from sqlalchemy import Column, Index, String, text
from sqlalchemy.dialects.mysql import BIGINT, INTEGER

from app import db


class Commodity(db.Model):
    __tablename__ = 'commodity'

    __table_args__ = (
        Index('uq_index', 'COMMODITY', 'COUNTRY', 'YEAR_AND_MONTH', unique=True),
    )

    ID = Column(BIGINT(19), primary_key=True, comment='主键')
    COMMODITY = Column(String(32), nullable=False, comment='商品')
    COUNTRY = Column(String(8), nullable=False, comment='国家')
    COUNTRY_NAME = Column(String(16), nullable=False, comment='国家名称')
    UNIT1 = Column(String(8), nullable=False, comment='单元1')
    UNIT2 = Column(String(8), nullable=False, comment='单元2')
    CURRENT_MONTH_QUANTITY1 = Column(INTEGER(10), comment='当前月份数量1')
    CURRENT_MONTH_QUANTITY2 = Column(INTEGER(10), comment='当前月份数量2')
    CURRENT_MONTH_VALUE = Column(INTEGER(12), comment='当前月值')
    CUMULATIVE_YEAR_TO_DATE_QUANTITY1 = Column(BIGINT(15), comment='迄今累计数量1')
    CUMULATIVE_YEAR_TO_DATE_QUANTITY2 = Column(BIGINT(15), comment='迄今累计数量2')
    CUMULATIVE_YEAR_TO_DATE_VALUE = Column(BIGINT(19), comment='累计年初值')
    YEAR_AND_MONTH = Column(String(16), nullable=False, comment='年月')
    COUNTRY_SRC = Column(String(16), server_default=text("'Japan'"), comment='数据来源')
    EXP_OR_IMP = Column(String(8), server_default=text("'Export'"), comment='进出口')

    def __init__(self, **items):
        """
        动态增加属性
        :param items:
        """
        for key in items:
            if hasattr(self, key):
                setattr(self, key, items[key])

    # def __repr__(self):
    #     return '<{},{},{}>'.format(self.COMMODITY, self.COUNTRY, self.YEAR_AND_MONTH)

    def list_all_member(self):
        """
        获取属性
        :return:
        """
        attrs = {}
        for name, value in vars(self).items():
            attrs[name] = value
        return attrs
