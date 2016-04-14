# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('splitnsave', '0007_auto_20160414_1945'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_interested',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.IntegerField(default=0)),
                ('product_id', models.ForeignKey(to='splitnsave.products')),
                ('user_id', models.ForeignKey(to='splitnsave.users')),
            ],
        ),
        migrations.AlterField(
            model_name='chat_history',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 14, 19, 45, 22, 435000)),
        ),
    ]
