#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/8/19 20:21
# @Author : dorom
# @File : auth_business.py
# @Software: PyCharm

from apps.auth.models.users_models import User
import jwt,time
from apps.auth.settings.config import *


class AuthBusiness(object):

    @classmethod
    def generate_auth_token(self,user_id, expires_time=EXPIRES_TIME):
        """
        鉴权加密
        :param expires_time:
        :return:
        """
        payload = {"id": user_id,"exp":time.time()+expires_time}
        return jwt.encode(
            payload,
            key=SECRET_KEY, algorithm="HS256"
        ).decode('utf-8')

    @staticmethod
    def verify_auth_token(token):
        try:
            data = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        except:
            return
        return User.query.get(data['id'])