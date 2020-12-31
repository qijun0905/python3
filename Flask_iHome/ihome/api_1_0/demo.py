# -*- coding: utf-8 -*-
"""
Created on 2020-12-31 15:24

@Author: wangqijun
"""
from . import api
from ihome import db
# import logging
from flask import current_app


@api.route("/index")
def index():
    #print("hello")
    # logging.error()   # 记录错误信息
    # logging.warn()   # 警告
    # logging.info()   # 信息
    # logging.debug()   # 调试
    # current_app.logger.error("error info")
    # current_app.logger.warn("warn info")
    # current_app.logger.info("info info")
    # current_app.logger.debug("debug info")
    return "index page"


# logging.basicConfig(level=logging.ERROR)