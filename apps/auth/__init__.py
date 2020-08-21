#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/8/18 16:11
# @Author : dorom
# @File : __init__.py.py
# @Software: PyCharm


from flask import Blueprint

user = Blueprint('user',__name__)
from apps.auth import urls


import pymysql
pymysql.install_as_MySQLdb()

