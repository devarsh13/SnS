# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('splitnsave', '0025_auto_20160410_1817'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cabs',
            old_name='Music',
            new_name='music',
        ),
        migrations.RemoveField(
            model_name='books',
            name='bookname',
        ),
        migrations.RemoveField(
            model_name='books',
            name='sharing_type',
        ),
        migrations.RemoveField(
            model_name='cabs',
            name='car_name_id',
        ),
        migrations.RemoveField(
            model_name='cabs',
            name='car_service_id',
        ),
        migrations.RemoveField(
            model_name='cabs',
            name='car_type_id',
        ),
        migrations.RemoveField(
            model_name='user_interested',
            name='id',
        ),
        migrations.AddField(
            model_name='apartments',
            name='location',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='books',
            name='college',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='books',
            name='location',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='cabs',
            name='car_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='cabs',
            name='car_service',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='cabs',
            name='car_type',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='laundary',
            name='cotton_clothes',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='laundary',
            name='dry_cleaning',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='laundary',
            name='fabric_softner',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='laundary',
            name='light_clothes',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='laundary',
            name='silk_clothes',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='laundary',
            name='steam_press',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='laundary',
            name='white_clothes',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='apartments',
            name='in_time',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='apartments',
            name='out_time',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='books',
            name='tag1',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='books',
            name='tag2',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='books',
            name='tag3',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='cabs',
            name='endtime',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='cabs',
            name='starttime',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='categories',
            name='category_name',
            field=models.CharField(default='', max_length=100, choices=[('', ''), ('Cabs', 'Cabs'), ('Books', 'Books'), ('Laundary', 'Laundary'), ('Apartments', 'Apartments')]),
        ),
        migrations.AlterField(
            model_name='laundary',
            name='endtime',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='laundary',
            name='starttime',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='products',
            name='gender',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='products',
            name='location',
            field=models.CharField(default=None, max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='post_date',
            field=models.DateField(default=datetime.date(2016, 4, 12), null=True),
        ),
        migrations.AlterField(
            model_name='user_interested',
            name='product_id',
            field=models.ForeignKey(to='splitnsave.products', primary_key=True),
        ),
        migrations.AlterField(
            model_name='user_interested',
            name='user_id',
            field=models.ForeignKey(primary_key=True, serialize=False, to='splitnsave.users'),
        ),
    ]
