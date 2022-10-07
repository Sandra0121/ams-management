# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.apps import apps
from django.contrib import admin
from .models import *


@admin.register(Asset_auto_tracking)
class Asset_auto_trackingAdmin(admin.ModelAdmin):
    list_display = ('id', 'asset_id', 'reader_loc', 'read_at')
    ordering = ('read_at',)
    search_fields = ('asset_id', 'reader_loc')
    # filter_vertical = ('',)

@admin.register(deleted_assets)
class deleted_assetsAdmin(admin.ModelAdmin):
    list_display = ('user_delete', 'itemname', 'itemid', 'deleted_on')
    ordering = ('deleted_on',)
    search_fields = ('itemname', 'deleted_on')
    # filter_vertical = ('',)

@admin.register(lost_items)
class lost_itemsAdmin(admin.ModelAdmin):
    list_display = ('user_lost', 'itemname', 'itemid', 'lost_on')
    ordering = ('lost_on',)
    search_fields = ('itemname', 'lost_on')
    # filter_vertical = ('',)

@admin.register(lended_assets)
class lended_assetsAdmin(admin.ModelAdmin):
    list_display = ('recivername', 'lender', 'staffid',
                    'itemname', 'where_itgo', 'lend_on')
    ordering = ('lend_on',)
    search_fields = ('itemname', 'lend_on')

@admin.register(assigned_assets)
class assigned_assetsAdmin(admin.ModelAdmin):
    list_display = ('userid', 'username', 'itemid',
                    'item_name', 'asgn_location', 'assign_on')
    ordering = ('assign_on',)
    search_fields = ('item_name', 'assign_on')

@admin.register(assetrequest)
class assetrequestAdmin(admin.ModelAdmin):
    list_display = ('userid', 'username', 'description',
                    'request_status', 'request_on')
    ordering = ('request_on', 'username')
    search_fields = ('username', 'request_on')


@admin.register(locations)
class locationsAdmin(admin.ModelAdmin):
    list_display = ('loname', 'lostatus', 'created_on')
    ordering = ('created_on',)
    search_fields = ('loname', 'created_on')


@admin.register(category)
class categoryAdmin(admin.ModelAdmin):
    list_display = ('coname', 'cocategory', 'costatus',
                    'codescrp', 'created_on')
    ordering = ('created_on', 'cocategory')
    search_fields = ('coname', 'created_on', 'cocategory')


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('sub_cat_name', 'category_id', 'costatus',
                    'codescrp', 'created_on')
    ordering = ('created_on', 'sub_cat_name')
    search_fields = ('sub_cat_name', 'created_on', 'category_id')


@admin.register(nonassets)
class nonassetsAdmin(admin.ModelAdmin):
    list_display = ('uid','nocname', 'nocid','tag_id', 'nocdescp',
                    'noclocation', 'noccategory',
                    'is_verified_today', 'is_assigned',
                    'updated_on', 'created_on')
    ordering = ('created_on', 'updated_on', 'noccategory')
    search_fields = ('nocname', 'nocid', 'updated_on', 'created_on')


@admin.register(conassets)
class conassetsAdmin(admin.ModelAdmin):
    list_display = ('coname', 'coqunty', 'colocation',
                    'cocategory', 'costatus', 'codescrp', 'updated_on', 'created_on')
    ordering = ('created_on', 'updated_on', 'cocategory')
    search_fields = ('coname', 'cocategory', 'updated_on', 'created_on')
    

@admin.register(Asset_notification)
class Asset_notificationAdmin(admin.ModelAdmin):
    list_display = ('current_loc', 'default_loc', 'has_changed_loc',
                    'read_at', 'asset_id')
    ordering = ('read_at',)
    search_fields = ('current_loc', 'default_loc', 'asset_id')


@admin.register(edited_assets)
class edited_assetsAdmin(admin.ModelAdmin):
    list_display = ('user_edit', 'itemname', 'itemid', 'edited_on')
    ordering = ('edited_on',)
    search_fields = ('user_edit', 'itemname', 'deleted_on')

@admin.register(access_doors)
class access_doorsAdmin(admin.ModelAdmin):
    list_display = ('door_id', 'door_name')
    ordering = ('door_id',)
    search_fields = ('door_id', 'door_name')
    
@admin.register(authorization)
class authorizationAdmin(admin.ModelAdmin):
    list_display = ('cid', 'access_id')
    ordering = ('cid',)
    search_fields = ('cid', 'access_id')
    
@admin.register(attempts)
class attempts(admin.ModelAdmin):
    list_display= ('card_id', 'access_door_id', 'attempt_on', 'access_status','door_description')
    ordering = ('attempt_on',)
    search_fields = ('card_id', 'access_door_id', 'attempt_on')

# admin.site.register(category)
# admin.site.register(SubCategory)
