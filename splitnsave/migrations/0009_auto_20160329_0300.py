# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('splitnsave', '0008_auto_20160325_1805'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='id',
        ),
        migrations.AddField(
            model_name='users',
            name='user_id',
            field=models.IntegerField(default=0, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='profession_list',
            name='profession_name',
            field=models.CharField(default='', max_length=100, null=True, choices=[('', ''), ('abc', 'abc')]),
        ),
    ]
