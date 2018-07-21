# _*_ coding:utf-8 _*_
__author__ = 'lqxing'
__date__ = '2018/7/17 9:38'
import xadmin

from .models import Banners, EmailVerifyRecords


class GlobalSettings(object):
    site_title = '慕学网后台管理系统'
    site_footer = '慕学网'
    menu_style = 'accordion'


class BannersAdmin(object):
    list_display = ['title', 'order', 'add_time']
    search_fields = ['title']
    list_filter = ['order', 'add_time']


class EmailVerifyRecordsAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email']
    list_filter = ['send_type', 'send_time']


xadmin.site.register(Banners, BannersAdmin)
xadmin.site.register(EmailVerifyRecords, EmailVerifyRecordsAdmin)
xadmin.site.register(xadmin.views.CommAdminView, GlobalSettings)