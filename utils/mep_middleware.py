# -*- coding: utf-8 -*-
"""
@Time    : 2022/1/23 1:12 下午
@Author  : QiAoHui
@Email   : qiaohui@bitorobotics.ltd
@File    : mep_middleware
@Version : V0.0.1
@license : (C) Copyright 2017-2030, Bito Robotics Co.Ltd.
"""
import logging
import threading
import uuid

from django.utils.deprecation import MiddlewareMixin

local = threading.local()


class RequestIDFilter(logging.Filter):
    def filter(self, record):
        record.request_id = getattr(local, 'request_id', "none")
        return True


class RequestIDMiddleware(MiddlewareMixin):

    def process_request(self, request):
        local.request_id = request.META.get('HTTP_X_REQUEST_ID', uuid.uuid4().hex)

    def process_response(self, request, response):
        if hasattr(request, 'request_id'):
            response['X-Request-ID'] = local.request_id
        try:
            del local.request_id
        except AttributeError:
            pass
        return response
