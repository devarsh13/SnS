# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('splitnsave', '0028_auto_20160413_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='verification_code',
            field=models.CharField(default='asdfghjkl', max_length=1000),
        ),
    ]
