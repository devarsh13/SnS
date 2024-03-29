# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-15 05:42
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('splitnsave', '0005_auto_20160415_0505'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notifications',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='products',
            name='reporter_by',
        ),
        migrations.AddField(
            model_name='notifications',
            name='poster',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='n_poster', to='splitnsave.users'),
        ),
        migrations.AddField(
            model_name='notifications',
            name='seeker',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='n_seeker', to='splitnsave.users'),
        ),
        migrations.AddField(
            model_name='notifications',
            name='status',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='chat_history',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 15, 5, 42, 50, 89104)),
        ),
    ]
