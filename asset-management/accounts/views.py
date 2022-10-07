# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages, auth
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import *


# Create your views here.

# AUTHENTICATION PART
@login_required
def index(request):
    return render(request,'../template/pages/login-register.html',{'name':"Login or Signup"})



def user_login(request):
    if not request.user.is_authenticated:

        if request.method=='POST':
            email=request.POST['email']
            pwwd=request.POST['pwwd']


            user=auth.authenticate(username=email, password=pwwd)

            if user is not None:
                auth.login(request,user)
                request.session['id']=user.id
                messages.success(request,email+" your have loged in successfully")
                if user.is_superuser or user.is_staff:
                    return HttpResponseRedirect('home',{'name':"Home"})
                else:
                    return HttpResponseRedirect('mlinzipage',{'name':"Home"})
            else:
                messages.error(request,"Invalid Credentials")
                return render(request,'../template/pages/login-register.html',{'name':"Login or Signup"})

        elif (request.method == 'GET'):
            return render(request,'../template/pages/login-register.html',{'name':"Login or Signup"})


    else:
        return HttpResponseRedirect('home')


def logout_view(request):
    try:
        del request.session['id']
    except KeyError:
        pass
    logout(request)
    messages.success(request, 'You logged out successfull')
    return HttpResponseRedirect('login')


# User managements
@login_required(login_url='/login')
def useradd(request):
    if request.method=='POST':
        if request.user.is_superuser:
            fullname=request.POST['fullname']
            email=request.POST['email']
            contacts=request.POST['contacts']
            position=request.POST['positions']
            user_pwd=request.POST['psww']

            if User.objects.filter(email=email).exists():
                messages.error(request, 'You have already register but if not, please try to change your email or contact your adminstrator')
                return HttpResponseRedirect('adduser',{'name':"Home"})
            else:
                fname, lname=fullname.split(" ")
                user=User()
                user.first_name=fname
                user.last_name=lname 
                user.username=email
                user.email=email
                hashed_pwd = make_password(user_pwd)
                user.password=hashed_pwd
                if position=='Admin':
                    user.is_superuser='True'
                    user.is_staff='True'
                elif position=='Secretary':
                    user.is_staff='True'
                    user.is_superuser='False'
                user.save()

                
                uid=User.objects.get(username=email).id
                ap_user=User.objects.get(pk=uid)
                infoo=userinfo()
                infoo.userid=ap_user
                infoo.contact=contacts
                infoo.position=position
                if position=='Security':
                    infoo.is_security='True'
                infoo.save()

                messages.success(request,'Thanks, '+email+' added successfuly.')
                return HttpResponseRedirect('/adduser')
    else:
        return render(request,'../template/auth/adduser.html',{'name':"Add User",'navbar':'mnguser'})

@login_required(login_url='/login')
def ulist(request):
    allusers=User.objects.values()
    return render(request,'../template/auth/userlist.html',{'name':"View Users",'navbar':'mnguser','users':allusers})

def blockuser(request,user_id):
    user = User.objects.get(id=user_id)
    user.is_active=False
    user.save()
    return HttpResponseRedirect('/ulist')

def unblockuser(request,user_id):
    user = User.objects.get(id=user_id)
    user.is_active=True
    user.save()
    return HttpResponseRedirect('/ulist')

def userdelete(request,user_id):
    try:
        u = User.objects.get(id = user_id)
        u.delete()
        messages.success(request, "The user is deleted successfuly")
        return HttpResponseRedirect('/ulist')      

    except User.DoesNotExist:
        messages.error(request, "User does not exist")    
        return HttpResponseRedirect('/ulist')

    except Exception as e: 
        return render(request, 'front.html',{'err':e.message})
    return HttpResponseRedirect('/ulist') 

def setpermision(request):
    return render(request,'../template/auth/setpermision.html',{'name':"Users Permision",'navbar':'mnguser'})  

def listgroup(request):
    return render(request,'../template/auth/grouplist.html',{'name':"Users Groups",'navbar':'mnguser'})

def change_pwd(request):
    if request.method=='POST':
        old_pwd=request.POST['old_pwd']
        new_pwd=request.POST['new_pwd']

        user=auth.authenticate(username=request.user.username, password=old_pwd)

        if user is not None:
            user_id=User.objects.filter(username=request.user.username).update(password=new_pwd)
            messages.success(request, "Password Changed succesfully")
            return HttpResponseRedirect('change_pwd')
        else:
            messages.error(request, "Password Not Changed")
            return HttpResponseRedirect('change_pwd')
    return render(request,'../template/auth/change_pwd.html',{'name':"Change Password",'navbar':'mnguser'})



