# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-06-22 05:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='useradmin',
            name='is_joke',
            field=models.CharField(blank=True, default='1', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='useradmin',
            name='display_password',
            field=models.CharField(blank=True, default='0', max_length=255, verbose_name='铭文密码'),
        ),
    ]
