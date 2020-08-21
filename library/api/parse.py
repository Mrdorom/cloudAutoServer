#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/8/18 17:58
# @Author : dorom
# @File : parse.py
# @Software: PyCharm

from public_config import MSG_MAP


def format_response(res):
    res_key = res.keys()
    if "code" not in res_key:
        res["code"] = 0
    if "message" not in res_key:
        res["message"] = MSG_MAP.get(res("code"),'')
    if "data" not in res_key:
        res["data"] = []
    return res
