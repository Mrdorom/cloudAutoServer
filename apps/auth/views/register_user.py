#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/8/19 15:47
# @Author : dorom
# @File : users.py
# @Software: PyCharm
import time

from flask import jsonify
try:
    from flask.ext.restful import Api, Resource,fields,marshal_with
except:
    from flask_restful import Api,Resource,fields,marshal_with
from apps.auth.schema.user_schema import RegisterSerialize
from apps.auth.models.users_models import User
from apps.auth.business.auth_business import AuthBusiness
from library.api.db import db

user_serializer = RegisterSerialize()


class RegisterUser(Resource):
    def __init__(self):
        self.auth = AuthBusiness()

    def post(self):
        args = user_serializer.register_parser().parse_args()
        username = args.get("username")
        password = args.get("password")
        email = args.get("email")
        password = User.hash_password(password)
        quryset = User.query.filter_by(email=email).first()
        if quryset is not None:
            args['id'] = quryset.id
            args['username'] = quryset.username
            args['email'] = quryset.email
            args['password'] = quryset.password
            data = {"id":quryset.id,"role":quryset.role}
            return jsonify({"code":500,"data":data,"message":"{0} 已注册".format(email)})
        create_at = str(time.time())
        role = 1
        user = User(username=username,email=email,password=password,role=role,create_at=create_at)
        db.session.add(user)
        db.session.commit()
        data = {"username":username,"role":role}
        return jsonify({"code":200,"data":data,"message":"注册成功"})