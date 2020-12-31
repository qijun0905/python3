# -*- coding: utf-8 -*-
"""
Created on 2020-12-31 15:21

@Author: wangqijun
"""
from flask import Blueprint


# 创建蓝图对象
api = Blueprint("api_1_0", __name__)


# 导入蓝图的视图
from . import demo