# Generated by Django 2.0.7 on 2018-07-23 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0006_auto_20180723_0836'),
        ('course', '0004_auto_20180723_1103'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='organization.Teachers', verbose_name='授课老师'),
        ),
    ]