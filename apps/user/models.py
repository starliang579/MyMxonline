# _*_ coding:utf-8 _*_
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class UserProfile(AbstractUser):
    nickname = models.CharField(max_length=20, verbose_name='昵称')
    birthday = models.DateTimeField(verbose_name='生日', null=True, blank=True)
    gender = models.CharField(choices=(('male','男'), ('female','女')), verbose_name='性别', default='male', max_length=6)
    address = models.CharField(max_length=100, verbose_name='地址')
    mobile = models.IntegerField(verbose_name='手机', null=True, blank=True)
    headshot = models.ImageField(upload_to='user/headshot/%Y/%m/%d', verbose_name='头像', max_length=500, null=True, blank=True)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name


class Banners(models.Model):
    title = models.CharField(max_length=50, verbose_name='标题')
    image = models.ImageField(max_length=500, upload_to='banner/%Y/%m/%d', verbose_name='轮播图')
    url = models.URLField(verbose_name='url')
    order = models.IntegerField(verbose_name='播放顺序', default=0)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name


class EmailVerifyRecords(models.Model):
    code = models.CharField(max_length=20, verbose_name='验证码')
    email = models.EmailField(verbose_name='发送邮箱')
    send_type = models.CharField(choices=(('register', '注册'), ('forget', '找回密码')), max_length=8)
    send_time = models.DateTimeField(default=datetime.now, verbose_name='发送时间')

    class Meta:
        verbose_name = '邮箱验证码'
        verbose_name_plural = verbose_name
