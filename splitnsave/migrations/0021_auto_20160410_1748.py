# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-10 17:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('splitnsave', '0020_auto_20160410_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='post_date',
            field=models.DateField(default=None, null=True),
        ),
    ]