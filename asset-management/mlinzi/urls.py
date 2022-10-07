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
from django.conf.urls import url, include
from . import views

urlpatterns = [
    # landing page
    url('mlinzipage', views.mlinzipage, name='Mlinzi Page'),
    url('dayvefication/(?P<loc_id>\d+)/$', views.dayvefication, name='Mlinzi Page'),
    url('chpwd', views.chnagepwd, name='Change Password'),
    url('notok/(?P<loc_id>\w+)/$', views.notok, name='New Request'),
    # url('is_ok/(?P<item_id>\w+)/(?P<loc_id>\d+)/$', views.is_ok, name='New Request'),
    url('dayvefication/is_ok', views.is_ok, name='New Request'),
    url('daily_coments', views.daily_comments, name='Mlinzi Comments'),
    url('finish_daily_check', views.finish_check, name='Mlinzi Finish'),

]
