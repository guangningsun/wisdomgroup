# -*- coding:UTF-8 -*-
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from mptt.admin import DraggableMPTTAdmin
from feincms.module.page.models import Page
import datetime
from django.utils.html import format_html
from AppModel import *


# 领用记录
class DrawRecoderInfo(models.Model):
    user_name = models.CharField(max_length=200,verbose_name='领取人姓名')
    user_phone = models.CharField(max_length=200,verbose_name='领取人电话')
    user_idcard = models.CharField(max_length=200,verbose_name='领取人身份证')
    present_name = models.CharField(max_length=200,verbose_name='领取物品名称')
    present_number = models.CharField(max_length=200,verbose_name='领取数量')
    activity_name = models.CharField(max_length=200,verbose_name='所属活动名称')
    draw_time = models.DateTimeField(auto_now=True,verbose_name='领取时间')
    is_success = models.BooleanField(verbose_name='是否领取成功',default="False")
    contacts_name = models.CharField(max_length=200,verbose_name='联系人姓名')
    contacts_phone = models.CharField(max_length=200,verbose_name='联系人电话')
    contacts_address = models.CharField(max_length=200,verbose_name='联系人地址')



# 活动类
class ActivityInfo(models.Model):
    AUTH_CHOICES = [
    ('0', '实物类'),
    ('1', '电子类'),
    ]
    activity_name = models.CharField(max_length=200,verbose_name='活动名称')
    start_time = models.DateTimeField(auto_now=True,verbose_name='开始时间')
    end_time = models.DateTimeField(auto_now=True,verbose_name='结束时间')
    sumarry = models.CharField(max_length=200,verbose_name='活动简介')
    present_name = models.CharField(max_length=200,verbose_name='礼品名称')
    present_type = models.CharField(max_length=200, choices=AUTH_CHOICES,verbose_name='礼品类型')
    activity_image= models.ImageField(u'图片',null=True, blank=True, upload_to='present_image')
    stock_num = models.CharField(max_length=200,verbose_name='库存数量')
    stock_type = models.CharField(max_length=200,verbose_name='库存单位')
    draw_num = models.CharField(max_length=200,verbose_name='领取数量')
    is_active = models.BooleanField(verbose_name='是否上架',default="False")

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = '用户信息'
    


# 用户类
class UserInfo(models.Model):

    user_name = models.CharField(max_length=200,verbose_name='用户名')
    phone_number = models.CharField(max_length=200,verbose_name='电话号')
    id_card = models.CharField(max_length=200,verbose_name='身份证号')
    contacts_name = models.CharField(max_length=200,verbose_name='联系人姓名')
    contacts_phone = models.CharField(max_length=200,verbose_name='联系人电话')
    contacts_address = models.CharField(max_length=200,verbose_name='联系人地址')
    weixin_openid = models.CharField(max_length=200,verbose_name='微信ID')
    nick_name = models.CharField(max_length=200,verbose_name='微信名')

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = '用户信息'




class WeixinSessionKey(models.Model):
    weixin_openid = models.CharField(max_length=200,verbose_name='openid')
    weixin_sessionkey = models.CharField(max_length=200,verbose_name='sessionkey')
    update_time = models.DateTimeField(auto_now=True,verbose_name='更新时间')

    class Meta:
        verbose_name = '微信用户SK'
        verbose_name_plural = '微信用户SK'
