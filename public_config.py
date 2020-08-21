#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/8/18 16:44
# @Author : dorom
# @File : public_config.py
# @Software: PyCharm


SERVER_ENV = "dev"

MSG_MAP = {
    0: "ok",
    101: "can not find object",
    102: "save object error"
}


SECRET_KEY = 'BTclasstest'   #加密密钥
EXPIRES_TIME = 600  # token过期时间

SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@127.0.0.1:3306/fFlask?charset=utf8'
SQLALCHEMY_COMMIT_ON_TEARDOWN = True   # 显示原生的sql语句
SQLALCHEMY_TRACK_MODIFICATIONS = True   # 未知
