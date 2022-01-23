# -*- coding: utf-8 -*-
"""
@Time    : 2022/1/23 5:16 下午
@Author  : QiAoHui
@Email   : qiaohui@bitorobotics.ltd
@File    : __init__.py
@Version : V0.0.1
@license : (C) Copyright 2017-2030, Bito Robotics Co.Ltd.
"""
from django.views.generic import View  # 导入类试图
from utils.response import render_to_json


class BaseController(View):
    SOURCE = "modeling"

    # json 返回
    @render_to_json
    def call_api_json(self, call_handle):
        # todo 处理参数
        data = call_handle()
        return data
