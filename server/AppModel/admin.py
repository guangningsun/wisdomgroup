# -*- coding:UTF-8 -*-
from django.contrib import admin
from AppModel.models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin, ExportActionModelAdmin
import logging,json,datetime
from django.utils.html import format_html
from django import forms
from mptt.admin import MPTTModelAdmin
from mptt.admin import DraggableMPTTAdmin
from feincms.module.page.models import Page
from django.utils.html import format_html,escape, mark_safe
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
import time
import decimal


logger = logging.getLogger(__name__)
logger.setLevel(level = logging.DEBUG)
handler = logging.FileHandler("tjctwl.log")
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)



# 用户管理
@admin.register(UserInfo)
class UserInfoAdmin(ImportExportModelAdmin): 
    list_display = ['id','nick_name','user_name','weixin_openid','phone_number','auth']
    search_fields = ('nick_name','user_name','weixin_openid','phone_number','auth')
    fieldsets = [
       ('用户数据', {'fields': ['nick_name','user_name','weixin_openid','phone_number','auth'], 'classes': ['']}),
    ]
    list_per_page = 15


# 用户管理
@admin.register(CheckInfo)
class CheckInfoAdmin(ImportExportModelAdmin): 
    list_display = ['family_contact_name','family_tel_num','family_address','registerTime','checkin_status','family_member_num','family_id','name','gender','age','nation','id_num','tel_num','address','work_place','has_disease_radio','disease_name','medicine_name','has_take_medicine_radio','room','hotel']
    search_fields = ('family_contact_name','family_tel_num','family_address','registerTime','checkin_status','family_member_num','family_id','name','gender','age','nation','id_num','tel_num','address','work_place','has_disease_radio','disease_name','medicine_name','has_take_medicine_radio','room','hotel')
    fieldsets = [
       ('用户数据', {'fields': ['family_contact_name','family_tel_num','family_address','registerTime','checkin_status','family_member_num','family_id','name','gender','age','nation','id_num','tel_num','address','work_place','has_disease_radio','disease_name','medicine_name','has_take_medicine_radio','room','hotel'], 'classes': ['']}),
    ]
    list_per_page = 15



#admin.site.register(CommodityCategory , MPTTModelAdmin)


admin.site.site_title = "疫情登记系统"
admin.site.site_header = "疫情登记系统1.0.1"


