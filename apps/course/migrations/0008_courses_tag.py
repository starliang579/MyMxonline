# Generated by Django 2.0.7 on 2018-07-24 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0007_courses_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='tag',
            field=models.CharField(default='后端开发', max_length=10, verbose_name='课程标签'),
        ),
    ]
