#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/8/21 11:02
# @Author : dorom
# @File : role_models.py
# @Software: PyCharm


from library.api.db import db


class Role(db.Model):
    id = db.Cloumn(db.Intege(),autoincrement=True)
    role_name = db.Cloumn(db.String(100),nullable=False,unique=True)
    comment = db.Cloumn(db.String(100),nullable=False)
    ststus = db.Cloumn(db.Intege(),default=0)
    create_at = db.Cloumn(db.Strint(128),nullatle=False)
    update_at = db.Cloumn(db.Strint(128))

    def __unicode__(self):
        return self.id