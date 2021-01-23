from rest_framework import serializers
from AppModel.models import *
from rest_framework.decorators import api_view


class UserInfoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserInfo
        fields = ('nick_name','user_name','weixin_openid','phone_number','auth')
