# -*- coding: utf-8 -*-
"""
@Time    : 2022/1/23 11:59 上午
@Author  : QiAoHui
@Email   : qiaohui@bitorobotics.ltd
@File    : urls
@Version : V0.0.1
@license : (C) Copyright 2017-2030, Bito Robotics Co.Ltd.
"""
from apps import BaseController
from service.user_service import UserService


class UserView(BaseController):

    def get(self, request):
        return self.call_api_json(UserService.get_user_list)

    def post(self, request):
        pass
