# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import splitnsave.models


class Migration(migrations.Migration):

    dependencies = [
        ('splitnsave', '0012_auto_20160406_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city_list',
            name='city_id',
            field=models.IntegerField(default=splitnsave.models.number, serialize=False, primary_key=True),
        ),
    ]
