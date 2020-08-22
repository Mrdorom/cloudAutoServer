#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/8/21 11:12
# @Author : dorom
# @File : user_role_memdels.py
# @Software: PyCharm

from library.api.db import db


class UserRole(db.Model):

    id = db.Column(db.Integer(),autoincrement=True,primary_key=True)
    user_id = db.Column(db.Integer(),nullable=True)
    role_id = db.Column(db.Integer(),nullable=True)

    def __repr__(self):
        return self.id