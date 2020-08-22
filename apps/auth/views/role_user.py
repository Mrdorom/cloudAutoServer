#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/8/21 14:12
# @Author : dorom
# @File : role_user.py
# @Software: PyCharm


from flask_restful import Resource
from flask import jsonify
from apps.auth.schema.user_schema import UserRoleSerailizer
from apps.auth.models.user_role_memdels import UserRole
from library.api.db import db
from flask_jwt_extended import jwt_required


class UserRoleView(Resource):

    @jwt_required
    def post(self):
        """
        添加用户角色接口
        @parma user_id
        @parma role_id
        @response {
            "code": 200,
            "res":{"role":role_id},
            "message": "success"
        }
        """
        args =  UserRoleSerailizer().user_role_parser().parse_args()
        user_id = args.get("user_id")
        role_id = args.get("role_id")
        queryset = UserRole.query.filter_by(user_id=user_id).first()
        if queryset:
            data = {"user_id":queryset.user_id,
                    "role_id":queryset.role_id}
            res = {
                "code": 201,
                "res":data,
                "message":"用户有用户角色"
            }
            return jsonify(res)
        user_role = UserRole(user_id=user_id,role_id=role_id)
        db.session.add(user_role)
        db.session.commit()
        res = {
            "code": 200,
            "res":{"role":role_id},
            "message": "success"
        }
        return jsonify(res)
