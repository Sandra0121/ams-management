# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class userinfo(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    is_secretary = models.BooleanField(default=False)
    is_security = models.BooleanField(default=False)
    contact = models.CharField(max_length=40)
    position = models.CharField(max_length=40)
    card=models.CharField(max_length=40, null=True)
    def __int__(self):
        return self.id
        

