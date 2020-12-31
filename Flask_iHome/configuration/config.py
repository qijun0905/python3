# -*- coding: utf-8 -*-
"""
Created on 2020-12-31 14:17

@Author: wangqijun
"""
import redis


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


class DevelopmentConfig(Config):
    """开发模式的配置信息"""
    DEBUG = True


class ProductionConfig(Config):
    """生产环境配置信息"""
    pass


config_map = {
    "develop": DevelopmentConfig,
    "product": ProductionConfig
}