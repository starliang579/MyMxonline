# _*_ coding:utf-8 _*_
__author__ = 'lqxing'
__date__ = '2018/7/17 11:02'
import xadmin

from .models import Cities, Organizations, Teachers


class CitiesAdmin(object):
    list_display = ['name', 'add_time']
    search_fields = ['name']
    list_filter = ['add_time']


class OrganizationsAdmin(object):
    list_display = ['name', 'city', 'click_nums', 'fav_nums', 'address', 'add_time', 'students', 'category']
    search_fields = ['name', 'city__name', 'address', 'desc']
    list_filter = ['city__name', 'click_nums', 'fav_nums', 'add_time', 'category']


class TeachersAdmin(object):
    list_display = ['name', 'org', 'work_years', 'work_company', 'work_position', 'fav_nums', 'click_nums', 'add_time']
    search_fields = ['name', 'org__name', 'work_company', 'work_position']
    list_filter = ['work_years', 'work_company', 'work_position', 'fav_nums', 'click_nums', 'add_time']


xadmin.site.register(Cities, CitiesAdmin)
xadmin.site.register(Organizations, OrganizationsAdmin)
xadmin.site.register(Teachers, TeachersAdmin)