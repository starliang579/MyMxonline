# Generated by Django 2.0.7 on 2018-07-23 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0005_organizations_course_nums'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizations',
            name='image',
            field=models.ImageField(blank=True, max_length=500, null=True, upload_to='org/%Y/%m/%d', verbose_name='机构图片'),
        ),
    ]
