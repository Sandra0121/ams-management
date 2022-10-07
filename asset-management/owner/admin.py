# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import requested_assets
# Register your models here.


@admin.register(requested_assets)
class requested_assetsAdmin(admin.ModelAdmin):
    list_display = ('asset_name', 'descriptions', 'request_user_id',
                'request_user', 'request_status', 'created_on')
    ordering = ('created_on',)
    search_fields = ('asset_name', 'created_on', 'request_user')
    # filter_vertical = ('request_user',)
