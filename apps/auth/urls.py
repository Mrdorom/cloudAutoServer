#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/8/19 17:53
# @Author : dorom
# @File : urls.py
# @Software: PyCharm


from flask_restful import Api
from . import user
from apps.auth.views.register_user import RegisterUser
from apps.auth.views.login_user import Login
from apps.auth.views.role_user import UserRoleView



api = Api(user)
api.add_resource(RegisterUser,"/register")
api.add_resource(Login,"/login")
api.add_resource(UserRoleView,"/set_user_role",endpoint='set_role')
