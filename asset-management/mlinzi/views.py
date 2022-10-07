# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import *
from manage_asset.models import *
from django.http import HttpResponseRedirect

# Create your views here.

def mlinzipage(request):
    all_loc=locations.objects.values().filter(lostatus='True')
    loc_and_count=[]
    for loc in all_loc:
        asset_count=nonassets.objects.filter(noclocation=loc['id']).count()
        ver_count=nonassets.objects.filter(noclocation=loc['id'],is_verified_today='True').count()
        my_dict={'id':loc['id'],'loc_name':loc['loname'],'count':int(asset_count),'ver_count':ver_count}
        loc_and_count.append(my_dict)

    # print(loc_and_count)
    return render(request,'../template/security/index.html',{'name':"Mlinzi Page",'location_all':loc_and_count})

def dayvefication(request,loc_id):
    loca_name=locations.objects.values().filter(id=loc_id)
    # print("loc name", loca_name)
    colist=nonassets.objects.values().filter(is_verified_today='False',noclocation=loc_id,nocstatus='Operational')
    # print("colist", colist)


    asset_count=nonassets.objects.filter(noclocation=loc_id).count()
    ver_count=nonassets.objects.filter(noclocation=loc_id,is_verified_today='True').count()

    return render(request,'../template/security/verpanel.html',{'name':"Verification",'assets':colist,
    'loca_name':loca_name[0]['loname'],'loc_id':loca_name[0]['id'],'asets_ver:':int(asset_count)})

def notok(request,loc_id):
    if request.method=='POST':
        nocname=request.POST['nocname']
        nocid=request.POST['nocid']
        problems=request.POST['problems']

        newprob=assetissues()

        newprob.nocname=nocname
        newprob.nocid=nocid
        newprob.problems=problems
        newprob.save()

        nonassets.objects.filter(nocid=nocid).update(is_verified_today='True')
        return HttpResponseRedirect('/dayvefication/'+str(loc_id)+'/')
    return HttpResponseRedirect('/dayvefication/'+str(loc_id)+'/')
    # colist=nonassets.objects.filter(nocstatus="Operational").values()
    # return render(request,'../template/security/verpanel.html',{'name':"Verification",'assets':colist})

    # newasset=nonassets()
    # newasset.id=req_id
    # newasset.nocstatus="LOST"
    # newasset.save()
    # colist=nonassets.objects.filter(nocstatus="Operational").values()
    # return render(request,'../template/security/verpanel.html',{'name':"Verification",'assets':colist})

def is_ok(request):
    if request.method == "POST":
        item_id=request.POST['aset_id']
        loc_id=request.POST['loc_id']
        print(item_id, loc_id)
        nonassets.objects.filter(nocid=item_id).update(is_verified_today='True')
        return HttpResponseRedirect('/dayvefication/'+str(loc_id)+'/')
    else:
        return HttpResponseRedirect('mlinzipage')

def chnagepwd(request):
    return render(request,'../template/security/changepwd.html',{'name':"Change  Password"})

def daily_comments(request):
    if request.method=='POST':
        user_coment=User.objects.values('username').filter(id=request.session['id'])
        coment_body=request.POST['comment_body']

        new_coment=daily_comment()
        new_coment.comment_body=coment_body
        new_coment.user_comment=user_coment[0]['username']
        new_coment.save()

        messages.success(request, "Your comments are succesfully send..!!")
        return HttpResponseRedirect('mlinzipage')

def finish_check(request):
    nonassets.objects.filter(is_verified_today='True').update(is_verified_today='False')
    messages.success(request, "Checkup is done successfully..!!")
    return HttpResponseRedirect('mlinzipage')


