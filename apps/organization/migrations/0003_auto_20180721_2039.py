# Generated by Django 2.0.7 on 2018-07-21 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0002_organizations_students'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizations',
            name='image',
            field=models.ImageField(max_length=500, upload_to='org/%Y/%m/%d', verbose_name='机构图片'),
        ),
    ]