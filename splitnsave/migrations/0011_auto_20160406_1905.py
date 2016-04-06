# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import splitnsave.models


class Migration(migrations.Migration):

    dependencies = [
        ('splitnsave', '0010_auto_20160405_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institute_list',
            name='institute_id',
            field=models.IntegerField(default=splitnsave.models.institute_number, serialize=False, primary_key=True),
        ),
    ]
