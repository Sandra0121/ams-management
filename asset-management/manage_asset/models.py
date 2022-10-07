# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import uuid
from accounts.models import userinfo
# Create your models here.

class locations(models.Model):
    loname=models.CharField(max_length=40)
    lostatus=models.BooleanField(default=True)
    #lodescrp=models.CharField(max_length=200)
    created_on=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.loname




class nonassets(models.Model): 
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nocname = models.CharField(max_length=100)
    nocid = models.CharField(max_length=40)
    tag_id = models.CharField(max_length=255, unique=True, null=True, default= "")
    nocdescp=models.CharField(max_length=200)
    noclocation=models.ForeignKey(locations, on_delete=models.CASCADE)
    noccategory=models.CharField(max_length=40)
    nocstatus=models.CharField(max_length=40)
    is_verified_today=models.BooleanField(default=False)
    is_assigned=models.BooleanField(default=False)
    updated_on=models.DateField(default=timezone.now)
    created_on=models.DateTimeField(auto_now_add=True,null=True)
    # assets=models.ForeignKey(Asset_auto_tracking, on_delete=models.CASCADE, null=True)
    
    
    def __str__(self):
        return self.tag_id

class Asset_auto_tracking(models.Model):
    # asset_id = models.ForeignKey(nonassets, on_delete=models.CASCADE)
    # asset_id = models.CharField(max_length=200, null=False)
    reader_loc = models.CharField(max_length=200, null=False)
    read_at = models.DateTimeField(auto_now_add=True,null=False)
    asset_id = models.ForeignKey(nonassets, on_delete=models.CASCADE)


    def __int__(self):
        return self.id
    

class Asset_notification(models.Model):
    current_loc = models.CharField(max_length=200, null=False)
    default_loc = models.CharField(max_length=200, null=False)
    has_changed_loc = models.BooleanField(default=False)
    read_at = models.DateTimeField(auto_now_add=True,null=False)
    asset_id = models.ForeignKey(nonassets, on_delete=models.CASCADE)


    def __int__(self):
        return self.id

class conassets(models.Model):
    coname=models.CharField(max_length=40)
    coqunty=models.CharField(max_length=40)
    colocation=models.CharField(max_length=40)
    cocategory=models.CharField(max_length=40)
    costatus=models.CharField(max_length=40)
    codescrp=models.CharField(max_length=200)
    unitt=models.CharField(max_length=40)
    updated_on=models.DateField(default=timezone.now)
    created_on=models.DateTimeField(auto_now_add=True,blank=True,null=True)     

    def __str__(self):
        return self.coname


class category(models.Model):
    coname=models.CharField(max_length=40)
    cocategory=models.CharField(max_length=40)
    costatus=models.BooleanField(default=True)
    codescrp=models.CharField(max_length=40)
    created_on=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.coname


class SubCategory(models.Model):
    sub_cat_name = models.CharField(max_length=40)
    category_id = models.ForeignKey(category, on_delete=models.CASCADE, null=False)
    costatus = models.BooleanField(default=True)
    codescrp = models.CharField(max_length=40)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sub_cat_name


class assetrequest(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    username = models.CharField(max_length=90)
    description = models.CharField(max_length=100)
    request_status = models.IntegerField()
    request_on = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.username


class assigned_assets(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    username = models.CharField(max_length=90)
    itemid = models.CharField(max_length=100)
    item_name = models.CharField(max_length=100)
    asgn_location = models.CharField(max_length=100)
    assgn_status = models.IntegerField(default=1)
    assign_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class lended_assets(models.Model):
    recivername=models.CharField(max_length=100,)
    lender=models.CharField(max_length=100)
    staffid=models.CharField(max_length=20)
    itemname=models.CharField(max_length=100)
    itemid=models.CharField(max_length=100)
    where_itgo=models.CharField(max_length=100)
    descript=models.CharField(max_length=255)
    return_status=models.BooleanField(default=False)
    lend_on=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.recivername


class deleted_assets(models.Model):
    user_delete=models.CharField(max_length=100)
    itemname=models.CharField(max_length=100)
    itemid=models.CharField(max_length=100)
    deleted_on=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.itemname


class edited_assets(models.Model):
    user_edit=models.CharField(max_length=100)
    itemname=models.CharField(max_length=100)
    itemid=models.CharField(max_length=100)
    edited_on=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.itemname


class lost_items(models.Model):
    user_lost=models.CharField(max_length=100)
    itemname=models.CharField(max_length=100)
    itemid=models.CharField(max_length=100)
    lost_on=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.itemname


class security_report(models.Model):
    # day=models.CharField(max_length=100)
    content=models.CharField(max_length=100)
    detail=models.CharField(max_length=100)
    reported_on=models.DateTimeField(auto_now_add=True)

    def __int__(self):
        return self.id


class access_doors(models.Model):
    door_id=models.CharField(max_length=100, null=False)
    door_name=models.CharField(max_length=100)
    

    def __str__(self):
        return f"{self.door_id} - {self.door_name}"
    
class authorization(models.Model):
    cid=models.CharField(max_length=100, null=False)
    username= models.CharField(max_length=100)
    access_id=models.ForeignKey(access_doors, on_delete=models.CASCADE, null=False)
    
    
    def __str__(self):
        return f"{self.cid} - {self.username}  - {self.access_id.door_name}"
    
class attempts(models.Model):
    card_id=models.CharField(max_length=100, null=False)
    userFullName=models.CharField(max_length=100, null=True)
    access_door_id=models.ForeignKey(access_doors, on_delete=models.CASCADE)
    attempt_on=models.DateTimeField(auto_now_add=True)
    access_status=models.BooleanField(default=False)
    door_description=models.CharField(max_length=100)
    
    
    def __int__(self):
        return self.card_id
