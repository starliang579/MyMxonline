# _*_ coding:utf-8 _*_
__author__ = 'lqxing'
__date__ = '2018/7/21 19:05'
from django.conf.urls import url

from .views import OrgListView, AddUserAskView, OrgHomeView, OrgCoursesView, OrgDescView, OrgTeachersView, AddOrgFavView


app_name = 'organization'
urlpatterns = [
    # 机构列表
    url('^list/$', OrgListView.as_view(), name='org_list'),
    # userask表单提交
    url('^add_userask/$', AddUserAskView.as_view(), name='add_userask'),
    # 机构首页
    url('^detail/home/(?P<org_id>.*)$', OrgHomeView.as_view(), name='org_home'),
    # 机构课程
    url('^detail/courses/(?P<org_id>.*)$', OrgCoursesView.as_view(), name='org_courses'),
    # 机构介绍
    url('^detail/desc/(?P<org_id>.*)$', OrgDescView.as_view(), name='org_desc'),
    # 机构讲师
    url('^detail/teachers/(?P<org_id>.*)$', OrgTeachersView.as_view(), name='org_teachers'),
    # 机构收藏功能
    url('^add_org_fav/$', AddOrgFavView.as_view(), name='add_org_fav'),

]
