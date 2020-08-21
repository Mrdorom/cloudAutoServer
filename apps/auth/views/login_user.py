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
        """
        登录接口
        @param email
        @:param password
        @response:
        {
          "code": 200,
          "res": {
                "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwiZXhwIjoxNTk3OTI3NTc1LjgxMTM2fQ.hOScYPYd-mvmCorz6in1Jf9tTou1X360aWqOPZ5-8ms"
          },
          "message": "登录成功"
        }
        :return:
        """
        parser_args = self.login_serailzer.login_parser().parse_args()
        email = parser_args.get('email')
        password = parser_args.get('password')
        queryset = User.query.filter_by(email=email).first()
        if queryset:
            status_verify = queryset.verify_password(password)   #hash 密码校验
            if  status_verify:
                token = AuthBusiness.generate_auth_token(queryset.id)   # 生成秘钥
                res = {
                    "code":200,
                    "res":{"token":token},
                    "message":"登录成功"
                }
                return jsonify(res)

        res = {
            "code": 500,
            "res": {},
            "message": "账号密码是错误"
        }
        return jsonify(res)