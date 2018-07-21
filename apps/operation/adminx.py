# _*_ coding:utf-8 _*_
__author__ = 'lqxing'
__date__ = '2018/7/17 11:21'
import xadmin

from .models import UserAsks, UserCourses, Comments, UserMsgs, UserFavs


class UserAsksAdmin(object):
    list_display = ['name', 'mobile', 'course', 'add_time']
    search_fields = ['name', 'mobile', 'course']
    list_filter = ['add_time']


class UserCoursesAdmin(object):
    list_display = ['user', 'course', 'add_time']
    search_fields = ['user__name', 'course__name']
    list_filter = ['add_time']


class CommentsAdmin(object):
    list_display = ['user', 'course', 'add_time']
    search_fields = ['user__name', 'course__name', 'comment']
    list_filter = ['add_time']


class UserMsgsAdmin(object):
    list_display = ['user', 'msg', 'has_read', 'add_time']
    search_fields = ['user__name', 'msg']
    list_filter = ['has_read', 'add_time']


class UserFavsAdmin(object):
    list_display = ['user', 'fav_type', 'fav_id', 'add_time']
    search_fields = ['user__name']
    list_filter = ['fav_type', 'fav_id', 'add_time']


xadmin.site.register(UserAsks, UserAsksAdmin)
xadmin.site.register(UserCourses, UserCoursesAdmin)
xadmin.site.register(Comments, CommentsAdmin)
xadmin.site.register(UserMsgs, UserMsgsAdmin)
xadmin.site.register(UserFavs, UserFavsAdmin)
