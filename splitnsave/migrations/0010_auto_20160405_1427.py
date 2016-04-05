# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import splitnsave.models


class Migration(migrations.Migration):

    dependencies = [
        ('splitnsave', '0009_auto_20160329_0300'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='image_url',
            field=models.URLField(default=0),
        ),
        migrations.AddField(
            model_name='users',
            name='rating',
            field=models.CharField(default='0', max_length=4),
        ),
        migrations.AlterField(
            model_name='users',
            name='user_id',
            field=models.IntegerField(default=splitnsave.models.number, serialize=False, primary_key=True),
        ),
    ]
