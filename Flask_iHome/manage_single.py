# -*- coding: utf-8 -*-
"""
Created on 2020-12-31 11:45

@Author: wangqijun
"""

from flask import Flask
import redis
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_wtf import CSRFProtect
from .configuration.config import config_map

# 创建flask的应用对象
app = Flask(__name__)


class Config(object):
    """配置信息"""
    DEBUG = True

    # flask的session需要用到的秘钥字符串 (如果用到session 必须配置该项)
    # app.config["SECRET_KEY"] = "Flask的秘钥字符串"
    # flask默认把session保存到了cookie中 (不安全，所以要配置SECRET_KEY)
    # 对cookie中session_id进行混淆处理时,需要设置秘钥
    # 设置session
    SECRET_KEY = "XHSOI*Y9dfs9cshd9"

    # 数据库
    SQLALCHEMY_DATABASE_URI = "mysql://root:localhost@127.0.0.1:3306/flask_ihome"
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # redis
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

    # flask-session配置
    SESSION_TYPE = "redis"  # session保存位置。 可以是redis、mongodb、sqlalchemy、文件等(默认保存到浏览器的cookie中)
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    SESSION_USE_SIGNER = True  # 对cookie中session_id进行隐藏处理
    PERMANENT_SESSION_LIFETIME = 86400  # session数据的有效期，单位秒


app.config.from_object(Config)

# # 工厂模式
# def create_app(config_name):
#     """
#     创建flask的应用对象
#     :param config_name: str  配置模式的模式的名字 （"develop",  "product"）
#     :return:
#     """
#     app = Flask(__name__)
#     # 根据配置模式的名字获取配置参数的类
#     config_class = config_map.get(config_name)
#     app.config.from_object(config_class)
#     return app
#
# # 创建flask的应用对象
# app = create_app("develop")

# 数据库
db = SQLAlchemy(app)

# 创建redis连接对象
redis_store = redis.StrictRedis(host=config_class.REDIS_HOST, port=config_class.REDIS_PORT)

# 利用flask-session，将session数据保存到redis中
Session(app)

# 为flask补充csrf防护
CSRFProtect(app)


@app.index("/index")
def index():
    # session的设置与获取与Flask原生方式相同
    return "index page"


if __name__ == "__main__":
    app.run()