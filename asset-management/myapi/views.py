# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from rest_framework import viewsets
from .serializer import assetsSerializer
from .models import assets
from django.db.models.signals import pre_save

from django.utils.crypto import get_random_string
from django.conf import settings as appsettings
import qrcode



class assetsviewset(viewsets.ModelViewSet):
    queryset = assets.objects.all().order_by('name')
    serializer_class = assetsSerializer