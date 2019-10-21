from django.contrib import admin
from django.urls import path,re_path
from .views import image,index,login,check,userdelete


urlpatterns = [
#     /image/30x30  /image/130x130
#     (?P<width>[0-9]+)  ==> form   name=width  width = 30
    path(r'index/',index),
    path(r'login/',login),
    path(r'login/check/',check),
    re_path(r'user/delete/',userdelete),
    re_path(r'image/(?P<width>[0-9]+)x(?P<height>[0-9]+)',image,name='placeholder'),
  
]