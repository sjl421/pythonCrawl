# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-04-27 11:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_banner_emailverifyrecord'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(default='image/default.png', upload_to='image/%Y%m', verbose_name='头像'),
        ),
    ]