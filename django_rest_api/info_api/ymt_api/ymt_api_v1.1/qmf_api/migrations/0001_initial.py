# Generated by Django 2.0 on 2018-09-10 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrderList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_time', models.CharField(blank=True, max_length=255, null=True, verbose_name='时间')),
                ('order_no', models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='订单号')),
                ('pay_money', models.CharField(blank=True, max_length=255, null=True, verbose_name='金额')),
                ('charge', models.CharField(blank=True, max_length=255, null=True, verbose_name='手续费')),
                ('trade_type', models.CharField(blank=True, max_length=255, null=True, verbose_name='支付类型')),
                ('trade_status', models.CharField(blank=True, max_length=255, null=True, verbose_name='支付状态')),
                ('account_status', models.CharField(blank=True, max_length=255, null=True, verbose_name='结算状态')),
                ('username', models.CharField(blank=True, max_length=255, null=True, verbose_name='username')),
                ('beizhu', models.CharField(blank=True, max_length=255, null=True, verbose_name='beizhu')),
                ('beizhu2', models.CharField(blank=True, max_length=255, null=True, verbose_name='beizhu2')),
                ('belong', models.CharField(blank=True, max_length=255, null=True, verbose_name='归属')),
            ],
            options={
                'verbose_name': '订单详情',
                'verbose_name_plural': '订单详情',
            },
        ),
        migrations.CreateModel(
            name='paymentList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.CharField(blank=True, max_length=255, null=True, verbose_name='时间')),
                ('end_date', models.CharField(blank=True, max_length=255, null=True, verbose_name='时间')),
                ('trade_no', models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='订单号')),
                ('withdraw_status', models.CharField(blank=True, max_length=255, null=True, verbose_name='提现状态')),
                ('trade_money', models.CharField(blank=True, max_length=255, null=True, verbose_name='金额')),
                ('charge', models.CharField(blank=True, max_length=255, null=True, verbose_name='金额')),
                ('trade_status', models.CharField(blank=True, max_length=255, null=True, verbose_name='支付状态')),
                ('username', models.CharField(blank=True, max_length=255, null=True, verbose_name='username')),
            ],
            options={
                'verbose_name': '提现详情',
                'verbose_name_plural': '提现详情',
            },
        ),
        migrations.CreateModel(
            name='Wxsession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wx_session', models.CharField(blank=True, max_length=65, null=True, verbose_name='wx_session')),
            ],
            options={
                'verbose_name': '微信授权',
                'verbose_name_plural': '微信授权',
            },
        ),
    ]
