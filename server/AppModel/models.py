# -*- coding:UTF-8 -*-
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from mptt.admin import DraggableMPTTAdmin
from feincms.module.page.models import Page
import datetime
from django.utils.html import format_html
from AppModel import *


class CheckInfo(models.Model):
    family_contact_name = models.CharField(max_length=200,verbose_name='联系人姓名')
    family_tel_num = models.CharField(max_length=200,verbose_name='联系人电话')
    family_address = models.CharField(max_length=200,verbose_name='联系人住址')
    registerTime = models.CharField(max_length=200,verbose_name='注册时间')
    checkin_status = models.CharField(max_length=200,verbose_name='是否已分配')
    family_member_num = models.CharField(max_length=200,verbose_name='成员数量')
    family_id  = models.CharField(max_length=200,verbose_name='家庭id')
    name = models.CharField(max_length=200,verbose_name='成员姓名')  
    gender = models.CharField(max_length=200,verbose_name='成员性别')
    age = models.CharField(max_length=200,verbose_name='成员年龄')
    nation = models.CharField(max_length=200,verbose_name='民族')
    id_num = models.CharField(max_length=200,verbose_name='身份证号')
    tel_num = models.CharField(max_length=200,verbose_name='成员电话号')   
    address = models.CharField(max_length=200,verbose_name='成员地址')   
    work_place = models.CharField(max_length=200,verbose_name='成员工作地点')
    has_disease_radio = models.BooleanField(verbose_name='是否有病史')
    disease_name = models.CharField(max_length=200,verbose_name='病史名称')
    medicine_name = models.CharField(max_length=200,verbose_name='用药名称')
    has_take_medicine_radio = models.BooleanField(verbose_name='是否用药')
    room = models.CharField(max_length=200,verbose_name='分配房间名',default="-")
    hotel = models.CharField(max_length=200,verbose_name='分配酒店名称',default="-")
   

    class Meta:
        verbose_name = '入住登记'
        verbose_name_plural = '入住登记'
    
    def __str__(self):
        return self.family_contact_name


class UserInfo(models.Model):
    AUTH_CHOICES = [
    ('0', '住户'),
    ('1', '医生'),
    ]
    nick_name = models.CharField(max_length=200,verbose_name='微信名')
    user_name = models.CharField(max_length=200,verbose_name='用户名')
    weixin_openid = models.CharField(max_length=200,verbose_name='微信ID')
    phone_number = models.CharField(max_length=200,verbose_name='手机号')
    auth = models.CharField(max_length=200, choices=AUTH_CHOICES,verbose_name='用户权限')


    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = '用户信息'
    
    def __str__(self):
        return self.user_name


class WeixinSessionKey(models.Model):
    weixin_openid = models.CharField(max_length=200,verbose_name='openid')
    weixin_sessionkey = models.CharField(max_length=200,verbose_name='sessionkey')
    update_time = models.DateTimeField(auto_now=True,verbose_name='更新时间')

    class Meta:
        verbose_name = '微信用户SK'
        verbose_name_plural = '微信用户SK'
