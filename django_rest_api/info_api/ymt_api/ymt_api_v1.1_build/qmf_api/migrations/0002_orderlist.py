# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-07-13 09:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qmf_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_time', models.CharField(blank=True, max_length=255, null=True, verbose_name='时间')),
                ('order_no', models.CharField(blank=True, max_length=255, null=True, verbose_name='dingdan')),
                ('pay_money', models.CharField(blank=True, max_length=255, null=True, verbose_name='pay_money')),
                ('trade_type', models.CharField(blank=True, max_length=255, null=True, verbose_name='trade_type')),
                ('trade_status', models.CharField(blank=True, max_length=255, null=True, verbose_name='trade_status')),
            ],
            options={
                'verbose_name': '订单详情',
                'verbose_name_plural': '订单详情',
            },
        ),
    ]