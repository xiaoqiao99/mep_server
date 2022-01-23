# -*- coding: utf-8 -*-
"""
@Time    : 2022/1/23 12:35 下午
@Author  : QiAoHui
@Email   : qiaohui@bitorobotics.ltd
@File    : decorators
@Version : V0.0.1
@license : (C) Copyright 2017-2030, Bito Robotics Co.Ltd.
"""
import json
import datetime
from django.http import HttpResponse
from .decorator import decorator


@decorator
def render_to_json(func, *args, **kw):
    ajax_data = func(*args, **kw)
    response = None

    if isinstance(ajax_data, HttpResponse):
        response = ajax_data
    else:
        class DateEncoder(json.JSONEncoder):
            def default(self, obj):
                if isinstance(obj, datetime.datetime):
                    return obj.strftime('%Y-%m-%d %H:%M:%S')
                else:
                    return json.JSONEncoder.default(self, obj)

        response = HttpResponse(json.dumps(ajax_data, ensure_ascii=False, cls=DateEncoder),
                                content_type="application/json")
    return response
