from django.contrib import admin
from django.conf.urls import url, include
from . import views

urlpatterns = [
    # landing page    
    url('ownerpage', views.ownerpage, name='Owner Page'),

    # Chage the password
    url('changepassowrd', views.ow_chnagepwd, name='Owner Page'),

    # Request new Assets
    url('new_request', views.request_asset, name="New Request"),

]