#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/8/20 10:30
# @Author : dorom
# @File : user_schema.py
# @Software: PyCharm
from flask_restful import reqparse
from marshmallow import Schema,fields
from validate_email import validate_email
from marshmallow import  ValidationError


def email(email_str):
    """ return True if email_str is a valid email """
    if validate_email(email_str):
        return email_str
    else:
        raise ValidationError("{} is not a valid email")



class RegisterSerialize(Schema):

    def register_parser(self):
        """
        注册接口参数序列化解析
        :return:
        """
        register_parser = reqparse.RequestParser()
        register_parser.add_argument("username", type=str, required=True, help="username 必须为String")
        register_parser.add_argument("email", type=email, required=True, help="邮箱格式错误")
        register_parser.add_argument('password', type=str, required=True, help="密码必须为String")
        return register_parser

    def serializer(self):
        """
        注册接口反序列化
        :return:
        """

        user_fields = {"id": fields.Integer,
                       "username": fields.String,
                       "password": fields.String,
                       "email": fields.String
                       }
        return {"code":fields.Integer,"data":user_fields,"message":fields.String}



class LoginSerailizer(Schema):

    def login_parser(self):
        """
        登录接口参数解析
        :return:
        """
        login_parser = reqparse.RequestParser()
        login_parser.add_argument("email",type=email,required=True,help='邮箱格式错误')
        login_parser.add_argument("password",type=str,required=True,help='密码缺失')
        return login_parser


class UserRoleSerailizer(Schema):

    def user_role_parser(self):
        """
        设置用户角色参数解析
        :return:
        """
        user_role_parser = reqparse.RequestParser()
        # user_role_parser.add_argument('token',type=str,location='headers',required=True)
        user_role_parser.add_argument('user_id',type=int,location='json',required=True,help='用户id必须为int类型')
        user_role_parser.add_argument('role_id',type=int,location='json',required=True,help='roel_id必须为int类型')
        return user_role_parser