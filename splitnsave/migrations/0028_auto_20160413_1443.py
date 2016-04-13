# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import splitnsave.models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('splitnsave', '0027_user_report_post_user_report_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat_history',
            name='delivered_status',
        ),
        migrations.RemoveField(
            model_name='users',
            name='verification_link',
        ),
        migrations.AlterField(
            model_name='chat_history',
            name='message',
            field=models.CharField(default=None, max_length=100000),
        ),
        migrations.AlterField(
            model_name='chat_history',
            name='timestamp',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='products',
            name='post_date',
            field=models.DateField(default=datetime.date(2016, 4, 13), null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.EmailField(max_length=254, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='user_id',
            field=models.IntegerField(default=splitnsave.models.number),
        ),
    ]
