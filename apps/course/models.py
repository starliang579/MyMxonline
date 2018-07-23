from datetime import datetime

from django.db import models

from organization.models import Organizations, Teachers


# Create your models here.
class Courses(models.Model):
    name = models.CharField(max_length=20, verbose_name='课程名')
    desc = models.CharField(max_length=200, verbose_name='课程简介')
    detail = models.TextField(verbose_name='课程详情')
    degree = models.CharField(choices=(('junior', '初级'), ('intermediate', '中级'), ('senior', '高级')), verbose_name='难度', max_length=12)
    learn_time = models.IntegerField(verbose_name='学习时长')
    students = models.IntegerField(verbose_name='学习人数')
    image = models.ImageField(max_length=500, verbose_name='课程图片', upload_to="course/%Y/%m/%d", null=True, blank=True)
    fav_nums = models.IntegerField(verbose_name='收藏人数')
    add_times = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    org = models.ForeignKey(Organizations, verbose_name='所属机构', null=True, blank=True, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teachers, verbose_name='授课老师', null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = '课程'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Lessons(models.Model):
    course = models.ForeignKey(Courses, verbose_name='课程', on_delete=models.CASCADE)
    name = models.CharField(max_length=30, verbose_name='章节名')
    add_times = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '课程章节'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Videos(models.Model):
    lesson = models.ForeignKey(Lessons, verbose_name='章节', on_delete=models.CASCADE)
    name = models.CharField(max_length=30, verbose_name='视频名')
    add_times = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '课程视频'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Resources(models.Model):
    course = models.ForeignKey(Courses, verbose_name='课程', on_delete=models.CASCADE)
    name = models.CharField(max_length=30, verbose_name='资源名称')
    file = models.FileField(upload_to='course/resourses/%Y/%m/%d', verbose_name='资源文件')
    add_times = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '课程资源'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name