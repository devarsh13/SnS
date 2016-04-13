# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('splitnsave', '0005_auto_20160414_0427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat_history',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 14, 4, 34, 23, 269000)),
        ),
    ]
