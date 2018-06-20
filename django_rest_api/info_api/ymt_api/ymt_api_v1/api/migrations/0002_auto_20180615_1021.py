# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-06-15 02:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='useradmin',
            name='display_password',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='铭文密码'),
        ),
        migrations.AddField(
            model_name='useradmin',
            name='url',
            field=models.CharField(blank=True, max_length=65, null=True, verbose_name='url'),
        ),
        migrations.AlterField(
            model_name='useradmin',
            name='ymt_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='用户名称'),
        ),
        migrations.AlterField(
            model_name='useradmin',
            name='ymt_pwd',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
