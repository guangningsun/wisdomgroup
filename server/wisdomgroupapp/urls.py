from django.contrib import admin
from wisdomgroupapp import views
from django.conf.urls import include, url
from django.urls import path,re_path
from django.views.static import serve
from django.conf import settings
from AppModel import admin as appadmin
from django.views.generic.base import RedirectView

urlpatterns = [
    url('admin/', admin.site.urls),
    path('weixin_sns/<js_code>', views.weixin_sns),
    path('weixin_gusi/', views.weixin_gusi),
    path('get_user_info_by_wxid/<weixin_id>', views.get_user_info_by_wxid),
    
    re_path(r'^media/(?P<path>.+)$', serve, {'document_root': settings.MEDIA_ROOT}),
  
    path('get_family_info/<tel_num>', views.get_family_info),
    path('create_family_info/', views.create_family_info),
    path('get_all_family_info/', views.get_all_family_info),
    path('fuzzy_query/<tel_num>', views.fuzzy_query),
    path('update_family_info/', views.update_family_info),
    path('release_isolation/', views.release_isolation),
    
] 
 
