#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/8/18 17:52
# @Author : dorom
# @File : tFlask.py
# @Software: PyCharm


from flask import Flask,jsonify
from library.api.parse import format_response
from library.api.db import db

# from public_config import SERVE_ENV


class TFlask(Flask):
    """
    重写 Flask  接口返回的response 解析
    重写 Flask 启动的Run方法
    """
    def make_response(self, rv):
        """
        重写make_response 方法，添加rv dict类型处理
        :param rv: res
        :return:
        """
        if isinstance(rv,dict):
            rv = jsonify(format_response(rv))
        return super().make_response(rv)

    def run(self, host="0.0.0.0", port="5000", debug="True", workers=None,server_env=None,load_dotenv=True, **options):
        """
        重写run方法，添加环境判断，测试环境自动打开debug模式
        正式环境结合 Gunicorn 多线程启动Flask
        :param host: 启动ip
        :param port: 启动端口
        :param debug: 启动模式
        :param workers: 启动线程数据
        :param server_env: 启动环境
        :param load_dotenv:
        :param options:
        :return:
        """
        if server_env == "dev":
            super().run(host=host, port=port, debug=debug)
        else:
            import multiprocessing
            from gunicorn.app.base import BaseApplication

            class Application(BaseApplication):

                def __init__(self,app,local_options=None):
                    self.options = local_options
                    self.application = app
                    super(Application,self).__init__()

                def load_config(self):
                    config = dict([(key,value) for key,value in self.options.items()
                                   if key in self.cfg.settings and value is not None])

                    for key,value in config.items():
                        self.cfg.set(key.lower(),value)

                def load(self):
                    return self.application

                def init(self,parser,opts,args):
                    super(Application,self).init(parser, opts, args)

            current_options = {
                "bind": f"{host}:{port}",
                "workers": workers or(multiprocessing.cpu_count()*2)+1,
                "worker_class": "gevent",
                "timeout": "1800"
            }
            Application(self,current_options).run()

def register_extensions(app):
    """
    注入 mysql链接
    :param app:
    :return:
    """
    db.init_app(app)


def tflask_main(config):
    app = TFlask(config.SERVER_ENV)
    app.config.from_object(config)
    register_extensions(app)
    return app
