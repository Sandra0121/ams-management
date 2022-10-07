"""assets URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# from django.conf.urls import url, include
from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import verify_jwt_token


urlpatterns = [
    # home Route
    path('home', views.home, name='Home'),
    path('report',views.get_report, name='report'),
    path('tracking', views.tracking, name='Tracking'),
    path('tracking_async', views.tracking_async, name='Tracking Async'),
    # Add rotes
    path('addasset', views.addassets, name='Add Asset'),
    path('addcategory', views.addcat, name='Add Category'),
    path('addlocation', views.addloc, name='Add Location'),
    path('addcunsumable', views.addcunsumable, name='Add Location'),
    path('addnoncunsumable', views.noncunsumable, name='Add Location'),
    path('editcunsumable', views.editcunsumable, name='Add Location'),
    path('notification', views.get_notification, name='Notification'),
    path('notification_async', views.get_notification_async, name='Notification Async'),
    # Listing assets routes
    path('non_ed/<slug:uid>', views.edit_nonconsumable, name='Edit Non Consumable'),
    path('non_edit', views.non_edit, name='Edit Non Consumable'),
    path('noconsumable', views.noconsumablelist, name='Non-Consumable List'),
    path('consumable', views.consumablelist, name='Consumable List'),
    path('editasset/(?P<item_id>\w+)/$', views.conseditasset, name='Activate'),
    path('deleteasset/(?P<item_id>\d+)/$', views.deleteasset, name='Activate'),
    # path('del_non_cons/(?P<uid>\d+)/$',
        # views.del_non_cons, name='Activate'),
    path('del_non_cons/<slug:uid>',views.del_non_cons, name='Activate'),
    path('deleted_list', views.get_deleted, name='Deleted List'),
    path('edited_list', views.get_edited, name='Edited List'),
    path('lost_list_items', views.lost_list_items, name='Lost List'),
    path('category_view', views.category_view, name='Category List'),
    path('view_location', views.view_location, name='Location List'),
    path('view_items_by_location', views.view_by_location, name='Location List'),
    #path('del_non_cons/<slug:uid>',views.del_non_cons, name='Activate'),
    path('del_autho/<slug:id>',views.del_autho, name='Activate'),
    path('del_door/<door_id>',views.del_door, name='Activate'),
    # path('room_assets/(?P<loc_id>\d+)/$',
    #     views.single_room_assets, name='Mlinzi Page'),

    path('room_assets/<loc_id>/', views.single_room_assets, name='room assets'),
    path('doors', views.at_doors, name='Doors'),
    path('autholist', views.authorization_list, name='Authorization list'),
    path('attempts', views.view_attempts, name='Attempts List'),
    path('attempts_async', views.view_attempts_async, name='Attempts List Async'),
    path('add_doors', views.add_doors, name='Add Doors'),
    path('add_autho', views.add_autho, name='Add Authorization'),
    # user and assets routes security_report
    path('assignlist', views.assignlist, name='Assigned Asset'),
    path('assign', views.assignasset, name='Assign Asset'),
    path('view_new_requ', views.new_asset_req, name='New Request'),
    path('queuerequest/(?P<reqid>\d+)/$', views.queuerequest, name='Queue Request'),
    path('borrowasset', views.borrowasset, name='Borrow Asset'),
    path('toborrowdesc/(?P<item_id>\d+)/$', views.borrowdesc, name='Borrow Descriptions'),
    path('voucher/(?P<lenid>\d+)/$', views.process_voucher, name='Processing Voucher'),
    path('vlist', views.vlists, name='Voucher List'),
    path('borrowlist', views.borrowlist, name='Borrowed List'),
    path('lost_items/(?P<lost_id>\w+)/$', views.lost_itemss, name='Lost Items'),
    path('lend_losted/(?P<lost_id>\w+)/$', views.assigned_losted, name='Lost Items'),
    path('return_item/(?P<retur_id>\w+)/$', views.retun_item, name='Lost Items'),
    path('lend_return/(?P<retur_id>\w+)/$', views.lend_retun, name='Lost Items'),

    #reports routes
    path('security_report', views.generate_security_report, name='Report'),
    # path('assign', views.assignasset, name='Assign Asset'),
    # path('view_new_requ', views.new_asset_req, name='New Request'),
    # path('queuerequest/(?P<reqid>\d+)/$', views.queuerequest, name='Queue Request'),
    # path('borrowasset', views.borrowasset, name='Borrow Asset'),
    # path('toborrowdesc/(?P<item_id>\d+)/$', views.borrowdesc, name='Borrow Descriptions'),
    # path('voucher/(?P<lenid>\d+)/$', views.process_voucher, name='Processing Voucher'),
    # path('vlist', views.vlists, name='Voucher List'),
    # path('borrowlist', views.borrowlist, name='Borrowed List'),
    # path('lost_items/(?P<lost_id>\w+)/$', views.lost_itemss, name='Lost Items'),
    # path('lend_losted/(?P<lost_id>\w+)/$', views.assigned_losted, name='Lost Items'),
    # path('return_item/(?P<retur_id>\w+)/$', views.retun_item, name='Lost Items'),
    # path('lend_return/(?P<retur_id>\w+)/$', views.lend_retun, name='Lost Items'),


    ## Assets Auto - Tracking ##

    # API DjangoRestFramework
    path('device_tracking_updates/', views.device_tracking_updates.as_view()),
    path('api-token-refresh/', refresh_jwt_token),
    path('api-token-auth/', obtain_jwt_token),
    path('api-token-verify/', verify_jwt_token),
    path('access_control_updates/', views.access_control_updates.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
