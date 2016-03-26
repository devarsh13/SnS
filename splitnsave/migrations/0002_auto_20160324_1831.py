# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('splitnsave', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city_list',
            name='cities',
        ),
        migrations.AddField(
            model_name='city_list',
            name='city_name',
            field=models.CharField(default=None, max_length=100, choices=[('0', None), ('1', 'AHM')]),
        ),
        migrations.AlterField(
            model_name='city_list',
            name='city_id',
            field=models.IntegerField(default=0, serialize=False, primary_key=True),
        ),
    ]
