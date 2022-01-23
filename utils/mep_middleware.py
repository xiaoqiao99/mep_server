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
import time

from django.utils.deprecation import MiddlewareMixin

local = threading.local()

logger = logging.getLogger('log')


class RequestIDFilter(logging.Filter):
    """request_id 日志过滤器"""

    def filter(self, record):
        record.request_id = getattr(local, 'request_id', "none")
        record.path = getattr(local, 'path', "none")
        return True


class RequestIDMiddleware(MiddlewareMixin):
    """request_id"""

    def process_request(self, request):
        local.request_id = request.META.get('HTTP_X_REQUEST_ID', uuid.uuid4().hex)
        local.path = request.path

    def process_response(self, request, response):
        if hasattr(request, 'request_id'):
            response['X-Request-ID'] = local.request_id
        try:
            del local.request_id
            del local.path
        except AttributeError:
            pass
        return response


class CostTimeMiddleware(MiddlewareMixin):
    """接口耗时"""

    def process_request(self, request):
        request.start_time = time.time()

    def process_response(self, request, response):
        execute_time = time.time() - request.start_time
        logger.info('execute_time %f' % execute_time)
        return response
