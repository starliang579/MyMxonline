# Generated by Django 2.0.7 on 2018-07-23 14:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0002_auto_20180716_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfavs',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
    ]
