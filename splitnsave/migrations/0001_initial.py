# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='city_list',
            fields=[
                ('city_id', models.IntegerField(default=None, serialize=False, primary_key=True)),
                ('cities', models.CharField(default=None, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(unique=True, max_length=254)),
                ('password', models.CharField(default='splitnsave', max_length=50)),
                ('verified', models.BooleanField()),
                ('contact_number', models.BigIntegerField(default=0)),
                ('birthday', models.DateField(default=None)),
                ('gender', models.CharField(default=None, max_length=1, choices=[('M', 'Male'), ('F', 'Female')])),
                ('city', models.ForeignKey(to='splitnsave.city_list')),
            ],
        ),
    ]
