# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image,ImageDraw
from django.db import models

# Create your models here.
class assets(models.Model):
    asset_name=models.CharField(max_length=100)

    def __int__(self):
        return self.id


