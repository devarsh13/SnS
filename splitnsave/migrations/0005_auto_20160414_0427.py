# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('splitnsave', '0004_auto_20160413_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat_history',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 14, 4, 27, 54, 562000)),
        ),
        migrations.AlterField(
            model_name='products',
            name='post_date',
            field=models.DateField(default=datetime.date(2016, 4, 14), null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='birthday',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='users',
            name='city',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='users',
            name='gender',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='users',
            name='institute',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='users',
            name='profession',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
