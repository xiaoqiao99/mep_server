# -*- coding: utf-8 -*-
"""
@Time    : 2022/1/23 11:59 上午
@Author  : QiAoHui
@Email   : qiaohui@bitorobotics.ltd
@File    : urls
@Version : V0.0.1
@license : (C) Copyright 2017-2030, Bito Robotics Co.Ltd.
"""
from django.urls import path

from apps.users.views import UserView

app_name = 'users'

urlpatterns = [
    path('', UserView.as_view()),
]
