# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-04-26 08:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': '用户信息', 'verbose_name_plural': '用户信息'},
        ),
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(default='', max_length=100, verbose_name='地址'),
        ),
        migrations.AddField(
            model_name='user',
            name='birthday',
            field=models.DateField(blank=True, null=True, verbose_name='生日'),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('male', '男'), ('female', '女')], default='female', max_length=10, verbose_name='性别'),
        ),
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(default='image/default.png', upload_to='image/%Y%m'),
        ),
        migrations.AddField(
            model_name='user',
            name='mobile',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='手机号'),
        ),
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(blank=True, max_length=50, verbose_name='昵称'),
        ),
    ]
