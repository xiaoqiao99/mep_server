from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models
from utils.model import BaseModel


class User(BaseModel):
    """
    用户
    """
    name = models.CharField('名称', max_length=32, unique=True)
    description = models.CharField('描述', max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
