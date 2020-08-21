#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/8/18 18:43
# @Author : dorom
# @File : db.py
# @Software: PyCharm

from contextlib import contextmanager
from flask_sqlalchemy import SQLAlchemy as BaseSQLAlchemy
from library.api.exceptions import SaveObjectException


class SQLAlchemy(BaseSQLAlchemy):

    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception:
            self.session.rollback()
            raise SaveObjectException

db = SQLAlchemy()
