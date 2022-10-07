# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def secretarypage(request):
    return render(request,'../template/secretaryy/index.html',{'name':"Secretary Page"})

# def dayvefication(request):
#     return render(request,'../template/security/verpanel.html',{'name':"Verification"})