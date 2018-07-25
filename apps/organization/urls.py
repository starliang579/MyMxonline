# _*_ coding:utf-8 _*_
__author__ = 'lqxing'
__date__ = '2018/7/21 19:05'
from django.conf.urls import url

from .views import OrgListView, AddUserAskView, OrgHomeView, OrgCoursesView, OrgDescView, OrgTeachersView, AddFavView
from .views import TeacherListView, TeacherDetailView


app_name = 'organization'
urlpatterns = [
    # 机构列表
    url('^list/$', OrgListView.as_view(), name='org_list'),
    # userask表单提交
    url('^add_userask/$', AddUserAskView.as_view(), name='add_userask'),
    # 机构首页
    url('^detail/home/(?P<org_id>\d+)$', OrgHomeView.as_view(), name='org_home'),
    # 机构课程
    url('^detail/courses/(?P<org_id>\d+)$', OrgCoursesView.as_view(), name='org_courses'),
    # 机构介绍
    url('^detail/desc/(?P<org_id>\d+)$', OrgDescView.as_view(), name='org_desc'),
    # 机构讲师
    url('^detail/teachers/(?P<org_id>\d+)$', OrgTeachersView.as_view(), name='org_teachers'),
    # 机构收藏（课程、教师）功能
    url('^add_fav/$', AddFavView.as_view(), name='add_fav'),

    # 教师相关url
    # 教师列表页
    url('^teacher/list/$', TeacherListView.as_view(), name='teacher_list'),
    # 教师详情页
    url('^teacher/detail/(?P<teacher_id>\d+)$', TeacherDetailView.as_view(), name='teacher_detail'),
]
