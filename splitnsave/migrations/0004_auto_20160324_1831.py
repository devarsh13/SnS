# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('splitnsave', '0003_auto_20160324_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city_list',
            name='city_name',
            field=models.CharField(default='', max_length=100, choices=[('0', ''), ('1', 'AHM')]),
        ),
    ]
