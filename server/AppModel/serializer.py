from rest_framework import serializers
from AppModel.models import *
from rest_framework.decorators import api_view


class ActivityInfoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ActivityInfo
        fields = ('activity_name','start_time','end_time','sumarry','present_name','present_type','activity_image','stock_num','stock_type','draw_num','is_active')
from rest_framework import serializers
from AppModel.models import *
from rest_framework.decorators import api_view


class ActivityInfoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ActivityInfo
        fields = ('activity_name','start_time','end_time','sumarry','present_name','present_type','activity_image','stock_num','stock_type','draw_num','is_active')


class UserInfoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ActivityInfo
        fields = ('nick_name','user_name','weixin_openid','phone_number','id_card','categary','apartment','room','sex','national','native_place','contacts_name','contacts_phone','contacts_address')

class DrawRecordInfoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ActivityInfo
        fields = ('user_name','user_phone','user_idcard','present_name','present_number','activity_name','draw_time','is_success')
