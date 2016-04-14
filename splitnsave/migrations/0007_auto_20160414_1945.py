# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('splitnsave', '0006_auto_20160414_0434'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_interested',
            name='product_id',
        ),
        migrations.RemoveField(
            model_name='user_interested',
            name='user_id',
        ),
        migrations.AddField(
            model_name='apartments',
            name='address',
            field=models.CharField(default='', max_length=1000, blank=True),
        ),
        migrations.AddField(
            model_name='apartments',
            name='enddate',
            field=models.CharField(default='', max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='apartments',
            name='startdate',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='apartments',
            name='in_time',
            field=models.CharField(default='', max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='apartments',
            name='number_of_bathrooms',
            field=models.CharField(default='', max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='apartments',
            name='number_of_bedrooms',
            field=models.CharField(default='', max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='apartments',
            name='out_time',
            field=models.CharField(default='', max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='apartments',
            name='rooms',
            field=models.CharField(default='', max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='enddate',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='books',
            name='startdate',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='cabs',
            name='enddate',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='cabs',
            name='startdate',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='chat_history',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 14, 19, 45, 4, 19000)),
        ),
        migrations.AlterField(
            model_name='laundary',
            name='enddate',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='laundary',
            name='startdate',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='products',
            name='gender',
            field=models.CharField(default='Male', max_length=1000),
        ),
        migrations.DeleteModel(
            name='user_interested',
        ),
    ]
