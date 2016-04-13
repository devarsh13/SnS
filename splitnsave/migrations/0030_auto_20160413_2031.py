# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('splitnsave', '0029_users_verification_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='rated_by',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='users',
            name='reported_by',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='chat_history',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 13, 20, 31, 4, 396000)),
        ),
    ]
