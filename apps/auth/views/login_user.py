#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/8/20 18:27
# @Author : dorom
# @File : login_user.py
# @Software: PyCharm

try:
    from flask.ext.restful import Api, Resource,fields,marshal_with
except:
    from flask_restful import Api,Resource,fields,marshal_with

from flask import jsonify
from apps.auth.models.users_models import User
from apps.auth.business.auth_business import AuthBusiness
from apps.auth.schema.user_schema import LoginSerailizer


class Login(Resource):

    def __init__(self):
        self.login_serailzer = LoginSerailizer()

    def post(self):
        parser_args = self.login_serailzer.login_parser().parse_args()
        email = parser_args.get('email')
        password = parser_args.get('password')
        queryset = User.query.filter_by(email=email).first()
        if queryset:
            status_verify = queryset.verify_password(password)
            token = AuthBusiness.generate_auth_token(queryset.id)
            if  status_verify:
                res = {
                    "code":200,
                    "data":{"token":token},
                    "message":"登录成功"
                }
                return jsonify(res)

        res = {
            "code": 500,
            "data": {},
            "message": "账号密码是错误"
        }
        return jsonify(res)