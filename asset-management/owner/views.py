# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import *
from django.contrib import messages,auth
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

# Create your views here.

@login_required
def ownerpage(request):
    asset_requested=requested_assets.objects.filter(request_user_id=request.session['id']).values('asset_name')

    return render(request,'../template/owner/index.html',{'name':"Owner Home",'asset_requested':asset_requested})

def ow_chnagepwd(request):
    return render(request,'../template/owner/changepwd.html',{'name':"Change  Password"})

def request_asset(request):
    if request.method=="POST":
        asset_name=request.POST['assetname']
        description=request.POST['description']

        login_user=User.objects.filter(id=request.session['id']).values()
        new_request=requested_assets()
        new_request.asset_name=asset_name
        new_request.descriptions=description
        new_request.request_user_id=login_user[0]['id']
        new_request.request_user=login_user[0]['first_name']+" "+login_user[0]['last_name']
        new_request.request_status=0
        new_request.save()
        return HttpResponseRedirect('ownerpage',{'name':"Home"})


