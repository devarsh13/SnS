# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import splitnsave.models


class Migration(migrations.Migration):

    dependencies = [
        ('splitnsave', '0011_auto_20160406_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city_list',
            name='city_id',
            field=models.IntegerField(default=splitnsave.models.city_number, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='profession_list',
            name='profession_id',
            field=models.IntegerField(default=splitnsave.models.profession_number, serialize=False, primary_key=True),
        ),
    ]
