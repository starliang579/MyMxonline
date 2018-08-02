# _*_ coding:utf-8 _*_
__author__ = 'lqxing'
__date__ = '2018/7/18 21:05'
from django import forms
from captcha.fields import CaptchaField

from .models import UserProfile


# 账户相关forms
class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=8)


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=8)
    captcha = CaptchaField()


class ForgetPwdForm(forms.Form):
    email = forms.EmailField(required=True)
    captcha = CaptchaField()


class ModifyPwdForm(forms.Form):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(required=True,min_length=8)
    password2 = forms.CharField(required=True,min_length=8)


# 用户中心相关forms
class HeadshotForm(forms.ModelForm):
    """
    修改用户头像
    """
    class Meta:
        model = UserProfile
        fields = ['headshot']


class UpdatePwdForm(forms.Form):
    """
    修改密码
    """
    password1 = forms.CharField(required=True,min_length=8)
    password2 = forms.CharField(required=True,min_length=8)


# 修改个人资料
class UpdateInfoForm(forms.ModelForm):
    """
    修改个人资料
    """
    class Meta:
        model = UserProfile
        fields = ['nickname', 'birthday', 'gender', 'address', 'mobile']