from datetime import datetime

from django.db import models


# Create your models here.
class Cities(models.Model):
    name = models.CharField(max_length=10, verbose_name='城市名称')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '城市'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Organizations(models.Model):
    name = models.CharField(max_length=20, verbose_name='机构名称')
    desc = models.CharField(max_length=200, verbose_name='机构简介')
    click_nums = models.IntegerField(verbose_name='点击次数')
    fav_nums = models.IntegerField(verbose_name='收藏人数')
    image = models.ImageField(max_length=500, verbose_name='机构图片', upload_to='org/%Y/%m/%d')
    address = models.CharField(max_length=200, verbose_name='机构地址')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    city = models.ForeignKey(Cities, verbose_name='城市', on_delete=models.CASCADE)
    students = models.IntegerField(verbose_name='学习人数', default=0)

    class Meta:
        verbose_name = '授课机构'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Teachers(models.Model):
    org = models.ForeignKey(Organizations, verbose_name='所属机构', on_delete=models.CASCADE)
    name = models.CharField(max_length=10, verbose_name='教师姓名')
    work_years = models.IntegerField(verbose_name='工作年限')
    work_company = models.CharField(max_length=20, verbose_name='所属公司')
    work_position = models.CharField(max_length=20, verbose_name='职位')
    feature = models.CharField(max_length=100, verbose_name='授课特点')
    fav_nums = models.IntegerField(verbose_name='收藏人数')
    click_nums = models.IntegerField(verbose_name='点击次数')
    headshot = models.ImageField(upload_to='teacher/%Y/%m/%d', verbose_name='头像')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '授课教师'
        verbose_name_plural = verbose_name
