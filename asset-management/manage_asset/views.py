# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import *
from mlinzi.models import *
from owner.models import *
from django.http import HttpResponseRedirect
from time import gmtime, strftime
from django.utils import timezone
import qrcode
from django.db.models import Count
import datetime
from django.http import JsonResponse
from datetime import datetime, timedelta
import json
from accounts.models import *

########## Ethan ##########
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from manage_asset.serializers import Asset_auto_trackingSerializer
from rest_framework.permissions import IsAuthenticated


# Create your views here.
@login_required #(login_url='/login')
def home(request):
    if request.user.is_authenticated:
       try:
        # Find total assets
            event=assetissues.objects.count()
            events=assetissues.objects.values()

            # Count the number of items in the database based on status
            Oparational=nonassets.objects.filter(nocstatus='Operational').count()
            Borrowed=nonassets.objects.filter(nocstatus='Borrowed').count()
            NonOparatianal=nonassets.objects.filter(nocstatus='NonOparatianal').count()
            Lost=nonassets.objects.filter(nocstatus='Lost').count()
            Maintanance=nonassets.objects.filter(nocstatus='Maintanance').count()

            # Find the percentage of items based on the status
            total_count=nonassets.objects.all().count()

            Per_Oparational=percentage_finder(Oparational,total_count)
            Per_Borrowed=percentage_finder(Borrowed,total_count)
            Per_NonOparatianal=percentage_finder(NonOparatianal,total_count)
            Per_Lost=percentage_finder(Lost,total_count)
            Per_Maintanance=percentage_finder(Maintanance,total_count)


            # Find General Informations about deleted assets
            daleted_assets=deleted_assets.objects.all().count()
            t_total=total_count+daleted_assets
            per_deleted=percentage_finder(daleted_assets,t_total)


            # Find General Informations about Edited assets
            consu_count=conassets.objects.count()
            total_items=consu_count+total_count
            edited_details=edited_assets.objects.all().count()
            per_edited=percentage_finder(edited_details,total_items)

            # Percentages of consumable and non--Consumable
            per_consu=percentage_finder(consu_count,total_items)
            per_nonconsu=percentage_finder(total_count,total_items)
            # print(edited_details)

            # Top summary
            Locations=locations.objects.all().count()
            Category=category.objects.all().count()
            Lended=lended_assets.objects.filter(return_status='False').count()
            Users=User.objects.all().count()
            Assets=total_items
            Request=requested_assets.objects.filter(request_status=0).count()



            status={'Operational':Oparational,'Borrowed':Borrowed,'NonOparatianal':NonOparatianal,'Lost':Lost,'Maintanance':Maintanance,
            'Per_Oparational':Per_Oparational, 'Per_Borrowed': Per_Borrowed, 'Per_NonOparatianal': Per_NonOparatianal, 'Per_Lost': Per_Lost,
            'Per_Maintanance': Per_Maintanance, 'deleted_assets': daleted_assets, 'per_deleted': per_deleted, 'per_exdited': per_edited, 'edited_details': edited_details,
            'per_consu': per_consu, 'per_nonconsu': per_nonconsu, 't_consu': consu_count, 't_nonconsu': total_count, 'Locations': Locations,
            'Category': Category, 'Lended': Lended, 'Users': Users,'Assets': Assets, 'Request': Request}

            return render(request,'../template/index.html',{'name':"Home",'navbar':'Home',"events":event,"evntlist":events,'status':status})
       except Exception as e:
           f= open("error.txt","a+")
           f.write("ERROR (0001)"+"::"+str(timezone.now())+": "+str(e)+"\r\n")
           f.close()

       return render(request,'../template/index.html')
    else:
        return render(request,'../template/pages/login-register.html',{'name':"Login or Signup"})


def view_by_location(request):
    all_loc=locations.objects.values().filter(lostatus='True')
    loc_and_count=[]
    for loc in all_loc:
        asset_count=nonassets.objects.filter(noclocation=loc['id']).count()
        ver_count=nonassets.objects.filter(noclocation=loc['id'],is_verified_today='True').count()
        my_dict={'id':loc['id'],'loc_name':loc['loname'],'count':int(asset_count),'ver_count':ver_count}
        loc_and_count.append(my_dict)
    return render(request,'../template/assets_management/dashbord/by_location.html',{'name':"Home",'navbar':'Home','location_all':loc_and_count})

def single_room_assets(request,loc_id):
    print("This is it, location:", loc_id)
    loca_name=locations.objects.filter(id=loc_id).values()
    colist=nonassets.objects.filter(noclocation=loc_id,nocstatus='Operational').values()

    asset_count=nonassets.objects.filter(noclocation=loc_id).count()
    ver_count=nonassets.objects.filter(noclocation=loc_id,is_verified_today='True').count()

    return render(request,'../template/assets_management/dashbord/single_room_asstes.html',{
        'name':"Home",'navbar':'Home','assets':colist,'ver_count':ver_count,
        'loca_name':loca_name[0]['loname'],'loc_id':loca_name[0]['id'],'asets_ver':asset_count})


def percentage_finder(number, total_num):
    try:
        return format(float((number*100)/total_num), '.1f')
    except Exception as e:
        f= open("error.txt","a+")
        f.write("ERROR (0001)"+"::"+str(timezone.now())+": "+str(e)+"\r\n")
        f.close()
        return 0


def addassets(request):
    places_loc = locations.objects.filter(lostatus='True').values('id','loname')
    catg_non = category.objects.filter(costatus='True',cocategory="nonconsumable").values('id','coname')

    catg_name_cons = category.objects.filter(costatus='True',cocategory="consumable").values('id','coname')
    return render(request,'../template/pages/additems.html',
    {'name':"Add Asset",'navbar':'manageasset','loca_tion':places_loc,'category_non':catg_non,'category_cons':catg_name_cons})


def noncunsumable(request):
    if request.method=='POST':
        nocname=request.POST['nocname']
        nocid=request.POST['nocid']
        tag_id=request.POST['tag_id']
        nocdescp=request.POST['nocdescp']
        noclocation=request.POST['noclocation']
        noccategory=request.POST['noccategory']
        nocstatus=request.POST['nocstatus']

        if nonassets.objects.filter(nocid=nocid).exists():
            messages.error(request, 'Asset with the same ID exist')
            return HttpResponseRedirect('addasset')
        
        #if locations.objects.filter(id=noclocation).exists():
            
        newasset=nonassets()
        newasset.nocname = nocname
        newasset.nocid = nocid
        newasset.tag_id = tag_id
        newasset.nocdescp = nocdescp
        newasset.noclocation = noclocation
        newasset.noccategory = noccategory
        newasset.nocstatus = nocstatus
        newasset.is_assigned = 0
        newasset.save()
        #print(newasset)
        messages.success(request, 'Asset added successfuly')
        return HttpResponseRedirect('addasset')
    return render(request,'../template/pages/additems.html',{'name':"Add Asset",'navbar':'manageasset'})


def addcunsumable(request):
    if request.method=='POST':
        coname=request.POST['coname']
        coqunty=request.POST['coqunty']
        colocation=request.POST['colocation']
        cocategory=request.POST['cocategory']
        costatus=request.POST['costatus']
        codescrp=request.POST['codescrp']
        unitt=request.POST['unitt']

        newasset=conassets()
        newasset.coname=coname
        newasset.coqunty=coqunty
        newasset.colocation=colocation
        newasset.cocategory=cocategory
        newasset.costatus=costatus
        newasset.codescrp=codescrp
        newasset.unitt=unitt
        newasset.save()
        messages.success(request, 'Asset added successfuly')
        return HttpResponseRedirect('consumable')
    return render(request,'../template/pages/additems.html',{'name':"Add Asset",'navbar':'manageasset'})


def editcunsumable(request):
    if request.method=='POST':
        coname=request.POST['coname']
        coqunty=request.POST['coqunty']
        colocation=request.POST['colocation']
        cocategory=request.POST['cocategory']
        costatus=request.POST['costatus']
        codescrp=request.POST['codescrp']
        unitt=request.POST['unitt']
        idd=request.POST['id']

        newasset=conassets()
        newasset.id=idd
        newasset.coname=coname
        newasset.coqunty=coqunty
        newasset.colocation=colocation
        newasset.cocategory=cocategory
        newasset.costatus=costatus
        newasset.codescrp=codescrp
        newasset.unitt=unitt
        newasset.save()


        new_edited=edited_assets()
        useridd=request.session['id']
        username=User.objects.filter(id=useridd).values('username')

        new_edited.user_edit=username[0]['username']
        new_edited.itemname= coname
        new_edited.itemid=idd
        new_edited.save()

        messages.success(request, 'Asset edited successfuly')
        return HttpResponseRedirect('consumable')
    return render(request,'../template/pages/additems.html',{'name':"Add Asset",'navbar':'manageasset'})


# GET LIST OF ITEMS
def consumablelist(request):
    colist=conassets.objects.values()
    return render(request,'../template/pages/consumablelist.html',{
        'name':"Consumable List",'navbar':'manageasset','assets':colist
        })



# GET EDITED AND DELETED AND LOST LIST
def get_deleted(request):
    del_list=deleted_assets.objects.values()
    return render(request,'../template/pages/deleted_items.html',{'name':"Deleted List",'navbar':'Home','assets':del_list})

def get_edited(request):
    edt_list=edited_assets.objects.values()
    return render(request,'../template/pages/edited_items.html',{'name':"Edited List",'navbar':'Home','assets':edt_list})

def lost_list_items(request):
    lost_ite=lost_items.objects.values()
    return render(request,'../template/pages/lost_items.html',{'name':"Lost List",'navbar':'Home','assets':lost_ite})



# EDIT FUNCTIONS
@login_required
def conseditasset(request,item_id):
    if request.user.is_superuser:
        try:
            asset=conassets.objects.filter(id=item_id).values()
            # print(asset)
            iteid=asset[0]['id']
            coname=asset[0]['coname']
            coqunty=asset[0]['coqunty']
            unitt=asset[0]['unitt']
            colocation=asset[0]['colocation']
            cocategory=asset[0]['cocategory']
            costatus=asset[0]['costatus']
            codescrp =asset[0]['codescrp']

            catg_name_cons = category.objects.filter(costatus=True,cocategory="consumable").values('id','coname')
            places_loc = locations.objects.filter(lostatus=True).values('id','loname')
            return render(request,'../template/pages/editcons.html',{'name':"Edit Assets",'navbar':'manageasset',
                'id':iteid,'coname':coname,'coqunty':coqunty,'unitt':unitt,'colocation':colocation,
                'cocategory':cocategory,'costatus':costatus,'codescrp':codescrp,'category_cons':catg_name_cons,
                'loca_tion':places_loc})

        except conassets.DoesNotExist:
            messages.error(request, "Asset doesnot exist")
            return HttpResponseRedirect('/consumable')
        except Exception as e:
            print(e)
            messages.error(request, "Sorry Unknown Error occurs ..!!")
            return HttpResponseRedirect('/consumable')
    else:
        messages.error(request, "Sorry access deined ..!!")
        return HttpResponseRedirect('/consumable')

def edit_nonconsumable(request,uid):
    if request.user.is_superuser:
        print(uid)
        try:
            asset=nonassets.objects.filter(uid=uid).values()
            # print(asset)
            iteid=asset[0]['uid']
            nocid=asset[0]['nocid']
            nocname=asset[0]['nocname']
            tag_id=asset[0]['tag_id']
            nocdescp=asset[0]['nocdescp']
            noclocation_id=asset[0]['noclocation']
            noccategory=asset[0]['noccategory']
            nocstatus=asset[0]['nocstatus']

            noclocation=locations.objects.filter(id=noclocation_id).values()


            places_loc = locations.objects.filter(lostatus="True").values('id','loname')
            catg_non = category.objects.filter(costatus="True",cocategory="nonconsumable").values('id','coname')

            return render(request,'../template/pages/edit_nonconsumable.html',{'name':"Edit Assets",'navbar':'manageasset',
                'uid':iteid,'nocid':nocid,'nocname':nocname,'nocdescp':nocdescp,'tag_id':tag_id,'noclocation':noclocation[0],
                'noccategory':noccategory,'nocstatus':nocstatus,'nocdescp':nocdescp,'loca_tion':places_loc,'category_non':catg_non,})
        except nonassets.DoesNotExist:
            messages.error(request, "Asset doesnot exist")
            return HttpResponseRedirect('/noconsumable')
        except Exception as e:
            messages.error(request, str(e)+"Sorry Unknown Error occurs ..!!")
            return HttpResponseRedirect('/noconsumable')
    else:
        messages.error(request, "Sorry access deined ..!!")
        return HttpResponseRedirect('/noconsumable')

def non_edit(request):

    if request.method=='POST':
        nocname=request.POST['nocname']
        nocid=request.POST['nocid']
        nocdescp=request.POST['nocdescp']
        noclocation=request.POST['noclocation']
        noccategory=request.POST['noccategory']
        nocstatus=request.POST['nocstatus']
        #coid=request.POST['coid']
        tag_id=request.POST['tag_id']

        newasset=nonassets()
        #newasset.nocid=nocid
        newasset.nocname=nocname
        newasset.nocid=nocid
        newasset.tag_id=tag_id
        newasset.nocdescp=nocdescp
        newasset.noclocation=noclocation
        newasset.noccategory=noccategory
        newasset.nocstatus=nocstatus
        newasset.is_assigned=0
        newasset.save()

        messages.success(request, 'Asset Edited successfuly')
        return HttpResponseRedirect('noconsumable')
    return render(request,'../template/pages/additems.html',{'name':"Edit Asset",'navbar':'manageasset'})


# ---------------------------CATEGORY AND LOCATIONS--------------------------------- 

# ADD CATEGORY AND LOCATIONS
def addcat(request):
    if request.method=='POST':
        coname=request.POST['coname']
        cocategory=request.POST['cocategory']
        costatus=request.POST['costatus']
        codescrp=request.POST['codescrp']

        if category.objects.filter(coname=coname).exists():
            messages.error(request, coname+' category already exist')
            return HttpResponseRedirect('addcategory')
        else:
            necat=category()
            necat.coname=coname
            necat.cocategory=cocategory
            necat.costatus=costatus
            necat.codescrp=codescrp
            necat.save()
            messages.success(request, 'Category created successfuly')
            return HttpResponseRedirect('addcategory')
    return render(request,'../template/pages/addcategory.html',{'name':"Add Asset",'navbar':'manageasset'})

def addloc(request):
    if request.method=='POST':
        loname=request.POST['loname']
        lostatus=request.POST['lostatus']
        lodescrp=request.POST['lodescrp']

        if locations.objects.filter(loname=loname).exists():
            messages.error(request, loname+'  already exist')
            return HttpResponseRedirect('addlocation')
        else:
            necat=locations()
            necat.loname=loname
            necat.lostatus=lostatus
            necat.lodescrp=lodescrp
            necat.save()
            messages.success(request, loname+' location added successfuly')
            return HttpResponseRedirect('addlocation')
    return render(request,'../template/pages/addlocation.html',{'name':"Add Location",'navbar':'manageasset'})


# CATEGORY AND LOCATION LISTING
def category_view(request):
    catego=category.objects.values()
    return render(request,'../template/pages/category_list.html',
    {'name':"Edit Asset",'navbar':'manageasset','category':catego})

def view_location(request):
    loc=locations.objects.values()
    return render(request,'../template/pages/location_list.html',
    {'name':"Edit Asset",'navbar':'manageasset','location':loc})


# DELETE AND UPDATE ASSETS
def del_non_cons(request,uid):
    if request.user.is_superuser:
        try:
            print(uid)
            deleted_details=nonassets.objects.filter(uid=uid).values(
                'nocname',
                'nocid', 
                'tag_id',
                'nocdescp',
                'noclocation',
                'noccategory',
                'nocstatus',
                'updated_on',
                'is_assigned',
                )
            update_deleted(request, deleted_details[0]['nocname'],deleted_details[0]['nocid']) 
            nonassets.objects.filter(uid=uid).delete()
            messages.success(request, "The asset is deleted succesfully..!!")
            return HttpResponseRedirect('/noconsumable')

        except User.DoesNotExist:
            messages.error(request, "asset doesnot exist")
            return HttpResponseRedirect('/noconsumable')

        except Exception as e:
            messages.error(request, str(e))
            return HttpResponseRedirect('/noconsumable')
    else:
            messages.error(request, "Sorry access deined ..!!")
            return HttpResponseRedirect('/noconsumable')

def deleteasset(request,item_id):
    if request.user.is_superuser:
        try:
            deleted_details=conassets.objects.filter(id=item_id).values('coname','id')
            update_deleted(request, deleted_details[0]['coname'],deleted_details[0]['id'])
            conassets.objects.filter(id=item_id).delete()
            messages.success(request, "The asset is deleted succesfully..!!")
            return HttpResponseRedirect('/consumable')

        except User.DoesNotExist:
            messages.error(request, "asset doesnot exist")
            return HttpResponseRedirect('/consumable')

        except Exception as e:
            messages.error(request, str(e))
            return HttpResponseRedirect('/consumable')
    else:
        messages.error(request, "Sorry access deined ..!!")
        return HttpResponseRedirect('/consumable')

def update_deleted(request,nocname,nocid):
    new_delete=deleted_assets()
    useridd=request.session['id']
    username=User.objects.filter(id=useridd).values('username')

    new_delete.user_delete=username[0]['username']
    new_delete.itemname=nocname
    new_delete.itemid=nocid
    new_delete.save()


def assignasset(request):
    if request.method=='POST':
        coname=request.POST['coname']
        usernam=request.POST['usernm']
        loca=request.POST['locat']
        itemid=request.POST['itemid']
        useid=User.objects.values().filter(id=usernam)

        newassgn=assigned_assets()
        newassgn.userid=User.objects.get(id=usernam)
        newassgn.username=useid[0]['username']
        newassgn.itemid=itemid
        newassgn.item_name=coname
        newassgn.asgn_location=loca
        newassgn.save()
        messages.success(request, "The asset is assigned to "+"jackroot7" +" succesfully..!!")

        nonassets.objects.filter(id=itemid).update(is_assigned=1)
        return HttpResponseRedirect('/assign') 
    colist=nonassets.objects.filter(is_assigned=0).values()
    ulist=requested_assets.objects.filter(request_status=1).values('request_user_id','request_user')
    locs=locations.objects.values()
    return render(request,'../template/pages/assignasset.html',
    {'name':"Assign Assets",'navbar':'userasset','assets':colist,'uselist':ulist,'locatins':locs})

def assignlist(request):
    colist=assigned_assets.objects.values().filter(assgn_status=1)
    return render(request,'../template/pages/assignlist.html',{'name':"Assigned Assets",'navbar':'userasset','assets':colist})


def new_asset_req(request):
    newrq=requested_assets.objects.filter(request_status=0).values()
    return render(request,'../template/pages/view_new_req.html',
    {'name':"New Requested Assets",'navbar':'userasset','use_request':newrq})


def queuerequest(request,reqid):
    requested_assets.objects.filter(id=reqid).update(request_status=1)
    messages.success(request, "Request added to queue succesfully..!!")
    return HttpResponseRedirect('/view_new_requ') 


def borrowasset(request):
    if request.method=='POST':
        lender=request.POST['lender']
        stafid=request.POST['stafid']
        nocdescp=request.POST['nocdescp']
        nocname=request.POST['nocname']
        nocid=request.POST['nocid']
        wherego=request.POST['wherego']

        useridd=request.session['id']
        username=User.objects.filter(id=useridd).values('username')
        newlwnd=lended_assets()
        newlwnd.recivername=lender
        newlwnd.lender=username[0]['username']
        newlwnd.staffid=stafid
        newlwnd.itemname=nocname
        newlwnd.itemid=nocid
        newlwnd.where_itgo=wherego
        newlwnd.descript=nocdescp
        newlwnd.lend_status=0
        newlwnd.save()

        nonassets.objects.filter(nocid=nocid).update(is_assigned='True',nocstatus='Borrowed')
        idddd=lended_assets.objects.filter(lender=lender,staffid=stafid,itemid=nocid,return_status='False').values('id')
        return HttpResponseRedirect('vlist')

    colist=nonassets.objects.filter(is_assigned='False').values()
    return render(request,'../template/pages/borrowasset.html',
    {'name':"Borrow Assets",'navbar':'userasset','assets':colist})

def borrowdesc(request,item_id):
    item_iid=nonassets.objects.filter(id=item_id).values('nocid','nocname')

    return render(request,'../template/pages/borrowedassetdescr.html',
    {'name':"Borrow Descriptions",'navbar':'userasset','item_name':item_iid[0]['nocname'],'item_id':item_id,'item_iid':item_iid[0]['nocid']})

def process_voucher(request,lenid):
    uid=request.session['id']
    uname=User.objects.filter(id=uid).values('username')

    vdeatails=lended_assets.objects.filter(id=lenid).values()
    # messages.success(request, "The asset is lended to  succesfully..!!")

    qr=qrcode.QRCode(
        version=1,
        box_size=15,
        border=2
    )
    # data=str(uid)+": "+str(uname)
    data=4
    qr.add_data(data)
    qr.make(fit=True)
    img=qr.make_image(fill='teal', back_color='white')
    img.save('static/images/qrcodimg.png')

    return render(request,'../template/pages/vouchers.html',
    {'name':"Prossesing  Voucher",'navbar':'userasset','vocher':vdeatails,'docty':"Lending Voucher",'qrc':"images/qrcodimg.png"})

def borrowlist(request):
    # It need much clarifications....@@@@@@@
    lend_list=lended_assets.objects.filter(return_status='False').values()
    return render(request,'../template/pages/borrowedlist.html',
    {'name':"Borrowed List",'navbar':'userasset','lend_list':lend_list})

def vlists(request):
    now = timezone.now()
    vouchers=lended_assets.objects.filter(return_status='False').order_by('-id','lend_on').values()
    return render(request,'../template/pages/voucherlist.html',
            {'name':"Voucher List",'navbar':'userasset','vouchers':vouchers})


def lost_itemss(request,lost_id):
    # Update to main table
    nonassets.objects.filter(nocid=lost_id).update(nocstatus='Lost')

    # Update lend table 
    lended_assets.objects.filter(itemid=lost_id).update(lend_status=1)
    lend_list=lended_assets.objects.filter(itemid=lost_id).values()

    # Update on Lost table
    new_lost=lost_items()
    new_lost.user_lost=lend_list[0]['recivername']
    new_lost.itemname=lend_list[0]['itemname']
    new_lost.itemid=lend_list[0]['itemid']
    new_lost.save()


    messages.success(request,'Report lost done ..!')
    return HttpResponseRedirect('/borrowlist')


def assigned_losted(request,lost_id):
    # Update to main table
    nonassets.objects.filter(nocid=lost_id).update(nocstatus='Lost')

    # Update assing table
    assigned_assets.objects.filter(itemid=lost_id).update(assgn_status=3)
    lend_list=assigned_assets.objects.filter(itemid=lost_id).values()

    # Update on Lost table
    new_lost=lost_items()
    new_lost.user_lost=lend_list[0]['username']
    new_lost.itemname=lend_list[0]['item_name']
    new_lost.itemid=lend_list[0]['itemid']
    new_lost.save()
    print(lend_list)
    return HttpResponseRedirect('assignlist')


def retun_item(request,retur_id):
    nonassets.objects.filter(nocid=retur_id).update(is_assigned='False',nocstatus='Operational')
    assigned_assets.objects.filter(itemid=retur_id).update(assgn_status=0)
    return HttpResponseRedirect('/assignlist')

def lend_retun(request,retur_id):
    nonassets.objects.filter(nocid=retur_id).update(is_assigned='False',nocstatus='Operational')
    lended_assets.objects.filter(itemid=retur_id).update(return_status='True')
    return HttpResponseRedirect('/borrowlist')



# REPORT FIELDS
def generate_security_report(request):
    return render(request,'../template/reports/security/index.html',
            {'name':"Report",'navbar':'reports'})

#Paul 
class device_tracking_updates(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        rfid_request = request.data
        
        asset_id = rfid_request['asset_id']
        reader_loc = rfid_request['reader_loc']
        read_at = rfid_request['read_at']

        try:
            existing_asset = nonassets.objects.filter(tag_id=asset_id).first()
            
            if existing_asset:
                tracking_updates = Asset_auto_tracking()
                tracking_updates.asset_id = existing_asset
                tracking_updates.reader_loc = reader_loc
                tracking_updates.read_at = read_at
                tracking_updates.save()
                save_status = "update saved!"
                #print(reader_loc, existing_asset.noclocation.loname)
                if existing_asset.noclocation.loname != reader_loc:
                    notification = Asset_notification()
                    notification.asset_id_id = existing_asset.uid
                    notification.current_loc = reader_loc
                    notification.default_loc = existing_asset.noclocation.loname
                    notification.has_changed_loc = True
                    notification.save()
                    print("notification saved")
                
                data = {'code': 200, 'asset_id': 'asset_id',
                'asset_name': 'asset_id', 'update_status': save_status, 'read_at': read_at}
                
                return JsonResponse({'data': data}, safe=False)
            
            data = {'code': 404, 'asset_id': None,
                'asset_name': None, 'update_status': None, 'read_at': None}
            
            return JsonResponse({'data': data})
                
        except Exception as e:
            print("exception", e)
            data = {"status_code": 500, "asset_id": None,
                "asset_name": None, "update_status": None, "read_at": None}
            
            return JsonResponse({"data": data})
        
        


def tracking(request):
    aset = Asset_auto_tracking.objects.values('id','asset_id', 'asset_id__nocname',
                                            'asset_id__nocid', 'reader_loc', 'read_at').order_by('-read_at')[:200]
    asets_ver= Asset_auto_tracking.objects.values('asset_id').distinct().count()
    
    #return render(request, 'assets_management/dashbord/index011.html', {'asets':aset, 'asets_ver':asets_ver})
    return render(request,'../template/pages/index001.html',{'name':"Notification",'navbar':'manageasset','asets':aset, 'asets_ver':asets_ver})


    
def tracking_async(request):
    aset = Asset_auto_tracking.objects.values('id','asset_id', 'asset_id__nocname',
                                            'asset_id__nocid', 'reader_loc', 'read_at').order_by('-read_at')[:200]
    asets_ver= Asset_auto_tracking.objects.values('asset_id').distinct().count()
    
    #return render(request, 'assets_management/dashbord/index011.html', {'asets':aset, 'asets_ver':asets_ver})
    return render(request,'../template/pages/index001table.html',{'name':"Notification",'navbar':'manageasset','asets':aset, 'asets_ver':asets_ver})
    

def noconsumablelist(request):
    colist=nonassets.objects.values().all()
    data_list=[]

    for item in colist:
        #loc_id=item['noclocation']
        #loc_name=locations.objects.values('loname__noclocation').get(id=item['noclocation'])['loname']
        #print(loc_name)
        loc_name=locations.objects.values('loname').get(id=item['noclocation_id'])['loname']
        data_dict={
            "uid":item['uid'],
            "nocname":item['nocname'],
            "nocid":item['nocid'],
            "tag_id":item['tag_id'],
            "nocdescp":item['nocdescp'],
            "noclocation":loc_name,
            "noccategory":item['noccategory'],
            "nocstatus":item['nocstatus'],
            "updated_on":item['updated_on'],
            "is_assigned":item['is_assigned'],
        }
        data_list.append(data_dict)
        
    return render(request,'../template/pages/noconsumable.html',{
        'name':"Non-Consumable List",'navbar':'manageasset','assets':data_list
        })

def get_report(request):
    try:
        tag_id = ""
        asset_id = request.POST['asset_id']
        asset_autotrack=Asset_auto_tracking.objects.filter(asset_id__uid=asset_id).values(
            'asset_id__tag_id',
            'asset_id__nocname',
            'asset_id__nocid',
            'asset_id__nocdescp',
            'asset_id__noclocation',
            'asset_id__noccategory',
            'asset_id__nocstatus',
            'asset_id__updated_on',
            'asset_id__is_assigned',
            'reader_loc',
            'read_at',
            'asset_id',
        ).order_by('-read_at')[:30]
        
        if asset_autotrack.exists():
            list_1 = list(asset_autotrack)
            newList = []
            
            for data in list_1:
                
                a = data['read_at'] + timedelta(hours=3)
                newdate = a.strftime("%Y-%m-%d %H:%M:%S")
                tag_id = data['asset_id__tag_id']
                data['read_at'] = newdate
                newList.append(data)
                
            return JsonResponse({'response': newList, "Code": 200, "TagId": tag_id})
        
        return JsonResponse({'response': None, "Code": 404})
    except Exception as e:
        return JsonResponse({'response': e, "Code": 500})
    
def get_notification(request):
    note= Asset_notification.objects.values(
        'id',
        'current_loc',
        'asset_id',
        'default_loc',
        'has_changed_loc',
        'asset_id__nocname',
        'asset_id__nocid',
        'read_at').order_by('-read_at')[:50]
    #print(note)

    return render(request,'../template/pages/notification.html',{'name':"Notification",'navbar':'manageasset','asets':note})

def get_notification_async(request):
    note= Asset_notification.objects.values(
        'id',
        'current_loc',
        'asset_id',
        'default_loc',
        'has_changed_loc',
        'asset_id__nocname',
        'asset_id__nocid',
        'read_at').order_by('-read_at')[:50]
    #print(note)

    return render(request,'../template/pages/notificationdata.html',{'name':"Notification",
                                                                    'navbar':'manageasset','asets':note})

def view_attempts(request):
    # card_id = request.POST['card_id']
    trials=attempts.objects.values('card_id',
                                'userFullName',
                                'access_door_id_id__door_name',
                                'attempt_on',
                                'access_status',
                                'door_description').order_by('-attempt_on')[:200]
    
    
    return render(request,'../template/pages/attempts.html',{
        'name':"Doors",'navbar':'access','autho':trials
        })
    
def view_attempts_async(request):
    # card_id = request.POST['card_id']
    trials=attempts.objects.values('card_id',
                                'userFullName',
                                'access_door_id_id__door_name',
                                'attempt_on',
                                'access_status',
                                'door_description').order_by('-attempt_on')[:200]
    
    
    return render(request,'../template/pages/attemptsdata.html',{
        'name':"Doors",'navbar':'access','autho':trials
        })
    
def at_doors(request):
    doors=access_doors.objects.values().all()

    return render(request,'../template/pages/at_doors.html',{
        'name':"Attempts List",'navbar':'access','autho':doors
        })
    
    
def authorization_list(request):
    list=authorization.objects.values('access_id_id__door_name',
                                    'cid',
                                    'username')
    
    return render(request,'../template/pages/autho.html',{
        'name':"Authorization List",'navbar':'access','autho':list
        })
    
def add_doors(request):
    if request.method=='POST':
        door_id=request.POST['door_id']
        door_name=request.POST['door_name']
        #lodescrp=request.POST['lodescrp']

        if access_doors.objects.filter(door_id=door_id).exists():
            messages.error(request, door_id+'  already exist')
            return HttpResponseRedirect('add_doors')
        else:
            necat=access_doors()
            necat.door_id=door_id
            necat.door_name=door_name
            #necat.lodescrp=lodescrp
            necat.save()
            messages.success(request, door_id+' door added successfuly')
            return HttpResponseRedirect('add_doors')
    return render(request,'../template/pages/add_doors.html',{'name':"Add Doors",'navbar':'access'})


def add_autho(request):
    if request.method=='POST':
        cid=request.POST['cid']
        username=request.POST['username']
        access_id=request.POST['access_id']

        if authorization.objects.filter(cid=cid).exists():
            messages.error(request, cid+'  already exist')
            return HttpResponseRedirect('add_autho')
        else:
            door_object=access_doors.objects.filter(door_id=access_id).first()
            necat=authorization()
            necat.cid=cid
            necat.username=username
            necat.access_id_id=door_object.id
            necat.save()
            messages.success(request, cid+' door added successfuly')
            return HttpResponseRedirect('add_autho')
    return render(request,'../template/pages/add_autho.html',{'name':"Add Authorization",'navbar':'access'})

def del_autho(request,id):
    if request.user.is_superuser:
        try:
            print(id)
            deleted_details=authorization.objects.filter(id=id).values(
                'cid',
                'username',
                'access_id',
                )
            update_deleted(request, deleted_details[0]['cid'],deleted_details[0]['access_id']) 
            nonassets.objects.filter(id=id).delete()
            messages.success(request, "The authorization is deleted succesfully..!!")
            return HttpResponseRedirect('/autho')

        except User.DoesNotExist:
            messages.error(request, "authorization doesnot exist")
            return HttpResponseRedirect('/autho')

        except Exception as e:
            messages.error(request, str(e))
            return HttpResponseRedirect('/autho')
    else:
            messages.error(request, "Sorry access deined ..!!")
            return HttpResponseRedirect('/autho')

def del_door(request,door_id):
    if request.user.is_superuser:
        try:
            #print(id)
            deleted_details=access_doors.objects.filter(door_id=door_id).values(
                'door_id',
                'door_name',
                )
            update_deleted(request, deleted_details[0]['door_id'],deleted_details[0]['door_name']) 
            access_doors.objects.filter(door_id=door_id).delete()
            messages.success(request, "The door is deleted succesfully..!!")
            return HttpResponseRedirect('/at_doors')

        except User.DoesNotExist:
            messages.error(request, "door doesnot exist")
            return HttpResponseRedirect('/at_doors')

        except Exception as e:
            messages.error(request, str(e))
            return HttpResponseRedirect('/at_doors')
    else:
            messages.error(request, "Sorry access deined ..!!")
            return HttpResponseRedirect('/at_doors')
        
#function to update data from readers for access control
class access_control_updates(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        rfid_request = request.data
        
        card_id = rfid_request['card_id']
        access_door_id = rfid_request['access_door_id']
        attempt_on = rfid_request['attempt_on']
        door_description=rfid_request['door_description']
        print(card_id, access_door_id, attempt_on, door_description)

        try:
            authorized_object = authorization.objects.filter(cid=card_id, access_id__door_id=access_door_id).first()
            print(authorized_object)
            
            access_failed = False
            userEmail = None
            save_status = "authentication Failed!"
            code = 401
            card_id = card_id
            door_description = door_description
            
            
            if authorized_object:
                access_failed = True
                code = 200
                save_status = "authentication true!"
                
            door_object=access_doors.objects.filter(door_id=access_door_id).first()
            userinfo1=userinfo.objects.filter(card=card_id).first()
            if userinfo1:
                userEmail = userinfo1.userid.email
                
            tracking_access = attempts()
            tracking_access.card_id = card_id
            tracking_access.access_door_id_id = door_object.id
            tracking_access.userFullName = userEmail
            tracking_access.attempt_on = attempt_on
            tracking_access.door_description = door_description
            tracking_access.access_status = access_failed
            tracking_access.save()
        
            data = {'code': code, 'card_id': card_id,
                'access_door_id': access_door_id, 'door_description':door_description,
                'update_status': save_status, 
                'attempt_on': attempt_on}
                
            return JsonResponse({'data': data}, safe=False)
                
        except Exception as e:
            print("exception", e)
            data = {"status_code": 500, "card_id": None,
                "access_door_id": None, "update_status": None, "attempt_on": None,
                "door_description": None}
            
            return JsonResponse({"data": data})