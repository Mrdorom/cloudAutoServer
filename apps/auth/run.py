#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/8/18 16:51
# @Author : dorom
# @File : run.py
# @Software: PyCharm


from library.api.tFlask import tflask_main
from apps.auth.settings import config
if config.SERVER_ENV != 'dev':
    from gevent import monkey
    monkey.patch_all()

from apps.auth import user


def create_app():
    app = tflask_main(config)
    register_blueprint(app)
    return app

def register_blueprint(app):
    app.register_blueprint(user,url_prefix='/user')

if __name__ == '__main__':
    create_app().run(port=config.PORT,server_env=config.SERVER_ENV)