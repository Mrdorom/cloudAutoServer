#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/8/19 14:59
# @Author : dorom
# @File : run.py
# @Software: PyCharm


from flask import Flask
from flask import Blueprint
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy

dept = Blueprint('dept', __name__)


@dept.route('/index',methods=['GET',])
def index():
    return jsonify('bb')

def run():
    app = Flask(__name__)
    app.register_blueprint(dept,url_prefix='/user')

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@127.0.0.1:3306/fFlask?charset=utf8'
    db = SQLAlchemy(app)
    app.run(debug=True)

if __name__ == '__main__':
    run()