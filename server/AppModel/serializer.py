from rest_framework import serializers
from AppModel.models import *
from rest_framework.decorators import api_view


class UserInfoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserInfo
        fields = ('nick_name','user_name','weixin_openid','phone_number','auth')


class CheckinSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CheckInfo
        fields = ('family_contact_name','family_tel_num','family_address','registerTime','checkin_status','family_member_num','family_id','name','gender','age','nation','id_num','tel_num','address','work_place','has_disease_radio','disease_name','medicine_name','has_take_medicine_radio','room','hotel')