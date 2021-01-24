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
