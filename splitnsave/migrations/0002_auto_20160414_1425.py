# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-14 14:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('splitnsave', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat_history',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 14, 14, 25, 48, 637592)),
        ),
    ]