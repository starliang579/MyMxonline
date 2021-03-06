# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-16 08:31
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='城市名称')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '城市',
                'verbose_name_plural': '城市',
            },
        ),
        migrations.CreateModel(
            name='Organizations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='机构名称')),
                ('desc', models.CharField(max_length=200, verbose_name='机构简介')),
                ('click_nums', models.IntegerField(verbose_name='点击次数')),
                ('fav_nums', models.IntegerField(verbose_name='收藏人数')),
                ('image', models.ImageField(max_length=500, upload_to='', verbose_name='机构图片')),
                ('address', models.CharField(max_length=200, verbose_name='机构地址')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.Cities', verbose_name='城市')),
            ],
            options={
                'verbose_name': '授课机构',
                'verbose_name_plural': '授课机构',
            },
        ),
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='教师姓名')),
                ('work_years', models.IntegerField(verbose_name='工作年限')),
                ('work_company', models.CharField(max_length=20, verbose_name='所属公司')),
                ('work_position', models.CharField(max_length=20, verbose_name='职位')),
                ('feature', models.CharField(max_length=100, verbose_name='授课特点')),
                ('fav_nums', models.IntegerField(verbose_name='收藏人数')),
                ('click_nums', models.IntegerField(verbose_name='点击次数')),
                ('headshot', models.ImageField(upload_to='teacher/%Y/%m/%d', verbose_name='头像')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('org', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.Organizations', verbose_name='所属机构')),
            ],
            options={
                'verbose_name': '授课教师',
                'verbose_name_plural': '授课教师',
            },
        ),
    ]
