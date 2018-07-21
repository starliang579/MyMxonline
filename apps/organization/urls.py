# _*_ coding:utf-8 _*_
__author__ = 'lqxing'
__date__ = '2018/7/21 19:05'
from django.conf.urls import url

from .views import OrgListView


app_name = 'organization'
urlpatterns = [
    url('^list/$', OrgListView.as_view(), name='org_list'),
]
