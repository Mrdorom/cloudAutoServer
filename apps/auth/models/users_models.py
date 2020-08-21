#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/8/19 16:16
# @Author : dorom
# @File : users_models.py
# @Software: PyCharm
import time

from werkzeug.security import generate_password_hash, check_password_hash

from library.api.db import db
import jwt,time
from apps.auth.settings.config import *

"""
|param|type|example|expline|
|table|str| __tablename__ ='user'|表名|
|primary_key|bool|primary_key=True|主键|
|nullable|bool|nullable=True|是否为空|
|default|  |default=xxx | 默认值|
|index|bool| index=True|索引|
|unique|bool|unique=True| 唯一|
|autoincrement|bool|autoincrement=True|id自增|
"""


class User(db.Model):
    """
    用户model
    """
    __tablename__ = "user"
    id = db.Column(db.Integer(),autoincrement=True,primary_key=True)
    username = db.Column(db.String(100),unique=True)
    email = db.Column(db.String(100),nullable=True)
    password = db.Column(db.String(256),nullable=False)
    create_at = db.Column(db.String(128),nullable=True)
    update_at = db.Column(db.String(128))


    @classmethod
    def hash_password(self, password):
        password = generate_password_hash(password)
        return password

    def verify_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return self.id

    def __unicode__(self):
        return self.id
