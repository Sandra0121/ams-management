# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import assetissues, daily_comment

@admin.register(assetissues)
class assetissuesAdmin(admin.ModelAdmin):
    list_display = ('nocname', 'nocid',
                    'problems', 'created_on')
    ordering = ('created_on', 'nocname')
    search_fields = ('nocname', 'created_on', 'nocid')


@admin.register(daily_comment)
class daily_commentAdmin(admin.ModelAdmin):
    list_display = ('comment_body', 'date_commented',
                    'user_comment', 'comment_is_read')
    ordering = ('date_commented',)
    search_fields = ('comment_body', 'comment_is_read', 'date_commented')
