# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import splitnsave.models


class Migration(migrations.Migration):

    dependencies = [
        ('splitnsave', '0006_auto_20160324_1850'),
    ]

    operations = [
        migrations.CreateModel(
            name='cabs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('startdate', models.DateField()),
                ('starttime', models.TimeField()),
                ('enddate', models.DateField()),
                ('endtime', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='categories',
            fields=[
                ('category_id', models.IntegerField(default=0, serialize=False, primary_key=True)),
                ('category_name', models.CharField(default='', max_length=100, choices=[('', ''), ('Cabs', 'Cabs'), ('Books', 'Books')])),
            ],
        ),
        migrations.CreateModel(
            name='chat_history',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.CharField(max_length=3000)),
                ('timestamp', models.DateTimeField(default=None)),
                ('delivered_status', models.BooleanField()),
                ('receiver', models.ForeignKey(related_name='receiver', default=None, to='splitnsave.users')),
                ('sender', models.ForeignKey(related_name='sender', default=None, to='splitnsave.users')),
            ],
        ),
        migrations.CreateModel(
            name='post_reporting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='products',
            fields=[
                ('product_id', models.IntegerField(default=0, serialize=False, primary_key=True)),
                ('number_of_sharers', models.IntegerField(default=1)),
                ('number_of_sharers_left', models.IntegerField(default=0)),
                ('gender', models.CharField(default=None, max_length=1, choices=[('M', 'Male'), ('F', 'Female')])),
                ('description', models.CharField(default=None, max_length=1000)),
                ('status', models.IntegerField(default=0)),
                ('image_url', models.URLField(default=0)),
                ('price', models.IntegerField(default=0)),
                ('category_id', models.ForeignKey(to='splitnsave.categories')),
                ('user_id', models.ForeignKey(to='splitnsave.users')),
            ],
        ),
        migrations.CreateModel(
            name='transaction_history',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('transact_status', models.IntegerField(default=0)),
                ('poster', models.ForeignKey(related_name='poster', default=None, to='splitnsave.users')),
                ('product_id', models.ForeignKey(default=None, to='splitnsave.products')),
                ('seeker', models.ForeignKey(related_name='seeker', default=None, to='splitnsave.users')),
            ],
        ),
        migrations.CreateModel(
            name='transaction_ratings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating', models.IntegerField(default=None, verbose_name=splitnsave.models.users)),
                ('product_id', models.ForeignKey(default=None, to='splitnsave.products')),
                ('ratee', models.ForeignKey(related_name='ratee', default=None, to='splitnsave.users')),
                ('rater', models.ForeignKey(related_name='rater', default=None, to='splitnsave.users')),
            ],
        ),
        migrations.CreateModel(
            name='user_reporting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.IntegerField(default=0)),
                ('reportee', models.ForeignKey(related_name='reportee', default=None, to='splitnsave.users')),
                ('reporter', models.ForeignKey(related_name='reporter', default=None, to='splitnsave.users')),
            ],
        ),
        migrations.AddField(
            model_name='post_reporting',
            name='product_id',
            field=models.ForeignKey(default=None, to='splitnsave.products'),
        ),
        migrations.AddField(
            model_name='post_reporting',
            name='reporter',
            field=models.ForeignKey(default=None, to='splitnsave.users'),
        ),
    ]
