# -*- coding: utf-8 -*-
"""
@Time    : 2022/1/23 4:47 下午
@Author  : QiAoHui
@Email   : qiaohui@bitorobotics.ltd
@File    : user_service
@Version : V0.0.1
@license : (C) Copyright 2017-2030, Bito Robotics Co.Ltd.
"""
from apps.users.models import *

import logging

logger = logging.getLogger('log')


class UserService(object):
    @classmethod
    def get_user_list(cls, *args, **kwargs):
        data = User.objects.all()
        data = [{"id": elem.id, "name": elem.name} for elem in data]
        logger.info('get_user_list')
        return data
