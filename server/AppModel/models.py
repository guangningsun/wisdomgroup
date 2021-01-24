# -*- coding:UTF-8 -*-
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from mptt.admin import DraggableMPTTAdmin
from feincms.module.page.models import Page
import datetime
from django.utils.html import format_html
from AppModel import *


class ActivityInfo(models.Model):
    AUTH_CHOICES = [
    ('0', '实物类'),
    ('1', '电子类'),
    ]
    activity_name = models.CharField(max_length=200,verbose_name='活动名称')
    start_time = models.CharField(max_length=200,verbose_name='开始时间')
    end_time = models.CharField(max_length=200,verbose_name='结束时间')
    sumarry = models.CharField(max_length=200,verbose_name='活动简介')
    present_name = models.CharField(max_length=200,verbose_name='礼品名称')
    present_type = models.CharField(max_length=200, choices=AUTH_CHOICES,verbose_name='礼品类型')
    activity_image= models.ImageField(u'图片',null=True, blank=True, upload_to='present_image')
    stock_num = models.CharField(max_length=200,verbose_name='库存数量')
    stock_type = models.CharField(max_length=200,verbose_name='库存单位')
    draw_num = models.CharField(max_length=200,verbose_name='领取数量')
    is_active = models.BooleanField(verbose_name='是否上架',default="False")
    




class WeixinSessionKey(models.Model):
    weixin_openid = models.CharField(max_length=200,verbose_name='openid')
    weixin_sessionkey = models.CharField(max_length=200,verbose_name='sessionkey')
    update_time = models.DateTimeField(auto_now=True,verbose_name='更新时间')

    class Meta:
        verbose_name = '微信用户SK'
        verbose_name_plural = '微信用户SK'
