# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class requested_assets(models.Model):
    asset_name=models.CharField(max_length=200)
    descriptions=models.CharField(max_length=200)
    request_user_id=models.CharField(max_length=200)
    request_user=models.CharField(max_length=200)
    request_status=models.IntegerField()
    created_on=models.DateTimeField(auto_now_add=True,null=True)

    def __int__(self):
        return self.id
