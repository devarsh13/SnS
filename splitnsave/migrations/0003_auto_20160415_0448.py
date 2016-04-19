# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-15 04:48
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('splitnsave', '0002_auto_20160414_1425'),
    ]

    operations = [
        migrations.CreateModel(
            name='notifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='transaction_history',
            name='transact_status',
        ),
        migrations.AlterField(
            model_name='chat_history',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 15, 4, 48, 45, 681510)),
        ),
        migrations.AlterField(
            model_name='products',
            name='post_date',
            field=models.DateField(default=datetime.date(2016, 4, 15), null=True),
        ),
        migrations.AlterField(
            model_name='transaction_history',
            name='product_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='splitnsave.products'),
        ),
        migrations.AddField(
            model_name='notifications',
            name='product_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='splitnsave.products'),
        ),
        migrations.AddField(
            model_name='notifications',
            name='user_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='splitnsave.users'),
        ),
    ]
