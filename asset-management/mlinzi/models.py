# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.
class assetissues(models.Model):
    nocname=models.CharField(max_length=200)
    nocid=models.CharField(max_length=20)
    problems=models.CharField(max_length=200)
    # nocstatus=models.CharField(max_length=40)
    # is_assigned=models.IntegerField(null=True)
    created_on=models.DateTimeField(auto_now_add=True,null=True)

    def __int__(self):
        return self.id


class daily_comment(models.Model):
    comment_body=models.CharField(max_length=200)
    date_commented=models.DateField(default=timezone.now)
    user_comment=models.CharField(max_length=200)
    comment_is_read=models.BooleanField(default=False)
    
    def __int__(self):
        return self.id
