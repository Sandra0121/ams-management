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
    # landing page Route
    url(r'^$', views.index, name='Home'),

    # Authentication route
    url('login', views.user_login, name='Login'),
    url('logout', views.logout_view, name='Logout'),

    # usermanagement routes
    url('adduser', views.useradd, name='Add User'),
    url('ulist', views.ulist, name='User List'),
    url('setpermision', views.setpermision, name='User Permision'),
    url('listgroup', views.listgroup, name='User Group'),
    url('block/(?P<user_id>\d+)/$', views.blockuser, name='Block'),
    url('activate/(?P<user_id>\d+)/$', views.unblockuser, name='Activate'),
    url('userdelete/(?P<user_id>\d+)/$', views.userdelete, name='User Delete'),
    url('change_pwd', views.change_pwd, name='Cangge Passowrd'),

]
