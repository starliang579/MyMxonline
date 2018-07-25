from datetime import datetime

from django.db import models

from user.models import UserProfile
from course.models import Courses


# Create your models here.
class UserAsks(models.Model):
    name = models.CharField(max_length=10, verbose_name='用户姓名')
    mobile = models.IntegerField(verbose_name='用户手机')
    course = models.CharField(max_length=20, verbose_name='咨询课程')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '用户咨询'
        verbose_name_plural = verbose_name


class UserCourses(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name='用户', on_delete=models.CASCADE)
    course = models.ForeignKey(Courses, verbose_name='课程', on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '用户课程'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.username + self.course.name


class Comments(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name='用户', on_delete=models.CASCADE)
    course = models.ForeignKey(Courses, verbose_name='课程', on_delete=models.CASCADE)
    comment = models.CharField(max_length=500, verbose_name='评论')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '用户评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '用户：' + self.user.username + '；课程：' + self.course.name


class UserMsgs(models.Model):
    user = models.IntegerField(default=0, verbose_name='用户')
    msg = models.CharField(max_length=300, verbose_name='消息')
    has_read = models.BooleanField(default=False, verbose_name='是否已读')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '用户消息'
        verbose_name_plural = verbose_name


class UserFavs(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='用户')
    fav_type = models.IntegerField(choices=((1, '课程'), (2, '机构'), (3, '讲师')), verbose_name='收藏类型')
    fav_id = models.IntegerField(verbose_name='收藏id号')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '用户收藏'
        verbose_name_plural = verbose_name
