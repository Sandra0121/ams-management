# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(userinfo)
class userinfoAdmin(admin.ModelAdmin):
    list_display = ('userid', 'is_secretary',
                    'is_security', 'contact', 'position')
    ordering = ('userid',)
    search_fields = ('position', 'userid')
