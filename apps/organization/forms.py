# _*_ coding:utf-8 _*_
__author__ = 'lqxing'
__date__ = '2018/7/22 11:39'
from django.forms.models import ModelForm

from operation.models import UserAsks


class UserAskForm(ModelForm):

    class Meta:
        model = UserAsks
        fields = ['name', 'mobile', 'course']