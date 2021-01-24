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
handler = logging.FileHandler("wisdomgroup.log")
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


# 活动管理
@admin.register(ActivityInfo)
class ActivityInfoAdmin(ImportExportModelAdmin): 
    list_display=['activity_name','start_time','end_time','sumarry','present_name','present_type','activity_image','stock_num','stock_type','draw_num','is_active']
    search_fields =('activity_name','start_time','end_time','sumarry','present_name','present_type','activity_image','stock_num','stock_type','draw_num','is_active')
    fieldsets = [
       ('用户数据', {'fields': ['activity_name','start_time','end_time','sumarry','present_name','present_type','activity_image','stock_num','stock_type','draw_num','is_active'], 'classes': ['']}),
    ]
    list_per_page = 15




admin.site.site_title = "智慧团群+"
admin.site.site_header = "智慧团群+"


