# _*_ coding:utf-8 _*_
__author__ = 'lqxing'
__date__ = '2018/7/17 10:21'
import xadmin

from .models import Courses, Lessons, Videos, Resources


class CoursesAdmin(object):
    list_display = ['name', 'degree', 'learn_time', 'students', 'fav_nums', 'add_times']
    search_fields = ['name', 'desc', 'detail']
    list_filter = ['degree', 'learn_time', 'students', 'fav_nums', 'add_times']


class LessonsAdmin(object):
    list_display = ['name', 'course', 'add_times']
    search_fields = ['name', 'course__name']
    list_filter = ['add_times', 'course__name']


class VideosAdmin(object):
    list_display = ['name', 'lesson', 'add_times']
    search_fields = ['name', 'lesson__name']
    list_filter = ['add_times']


class ResourcesAdmin(object):
    list_display = ['name', 'course', 'add_times']
    search_fields = ['name', 'course__name']
    list_filter = ['add_times']


xadmin.site.register(Courses, CoursesAdmin)
xadmin.site.register(Lessons, LessonsAdmin)
xadmin.site.register(Videos, VideosAdmin)
xadmin.site.register(Resources, ResourcesAdmin)