# _*_ coding:utf-8 _*_
__author__ = 'lqxing'
__date__ = '2018/7/28 19:41'
from django.conf.urls import url

from .views import UserInfoView, UpdateHeadshotView, UpdatePwdView, SendEmailCodeView, UpdateEmailView, MyCoursesView
from .views import MyFavOrgsView, MyFavTeachersView, MyFavCoursesView, MyMessagesView

app_name = 'user'
urlpatterns = [
    # 用户信息页面
    url('^info/$', UserInfoView.as_view(), name='user_info'),

    # 用户信息页面：修改头像
    url('^update_headshot/$', UpdateHeadshotView.as_view(), name='update_headshot'),

    # 用户信息页面：修改密码
    url('^update/pwd/$', UpdatePwdView.as_view(), name='updatepwd'),

    # 用户信息页面：修改邮箱-发送邮箱验证码
    url('^sendemail_code/$', SendEmailCodeView.as_view(), name='sendemail_code'),

    # 用户信息页面：修改邮箱
    url('^update_email/$', UpdateEmailView.as_view(), name='update_email'),

    # 我的课程
    url('^mycourses/$', MyCoursesView.as_view(), name='mycourses'),

    # 我的收藏-课程机构
    url('^myfav/orgs/$', MyFavOrgsView.as_view(), name='myfav_orgs'),
    # 我的收藏-授课讲师
    url('^myfav/teachers/$', MyFavTeachersView.as_view(), name='myfav_teachers'),
    # 我的收藏-公开课程
    url('^myfav/courses/$', MyFavCoursesView.as_view(), name='myfav_courses'),

    # 我的消息
    url('^mymessages/$', MyMessagesView.as_view(), name='mymessages'),

]