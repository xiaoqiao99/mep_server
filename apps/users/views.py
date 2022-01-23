# -*- coding: utf-8 -*-
"""
@Time    : 2022/1/23 11:59 上午
@Author  : QiAoHui
@Email   : qiaohui@bitorobotics.ltd
@File    : urls
@Version : V0.0.1
@license : (C) Copyright 2017-2030, Bito Robotics Co.Ltd.
"""
from .models import *
from utils.response import render_to_json


@render_to_json
def user_set(request):
    data = User.objects.all()
    data = [{"id": elem.id, "name": elem.name} for elem in data]
    return data
