# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-10 18:01
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('splitnsave', '0023_remove_products_post_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='post_date',
            field=models.DateField(default=datetime.date(2016, 4, 10), null=True),
        ),
    ]
