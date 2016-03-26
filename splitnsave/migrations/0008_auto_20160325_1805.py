# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('splitnsave', '0007_auto_20160325_1646'),
    ]

    operations = [
        migrations.CreateModel(
            name='apartments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rooms', models.IntegerField(default=1)),
                ('number_of_bedrooms', models.IntegerField(default=1)),
                ('number_of_bathrooms', models.IntegerField(default=1)),
                ('bathroom_type', models.CharField(default=None, max_length=100)),
                ('in_time', models.TimeField()),
                ('out_time', models.TimeField()),
                ('kitchen', models.BooleanField(default=False)),
                ('television', models.BooleanField(default=False)),
                ('heater', models.BooleanField(default=False)),
                ('air_conditioner', models.BooleanField(default=False)),
                ('internet', models.BooleanField(default=False)),
                ('medical_aid', models.BooleanField(default=False)),
                ('fire_alarm', models.BooleanField(default=False)),
                ('washing_machine', models.BooleanField(default=False)),
                ('parking', models.BooleanField(default=False)),
                ('canteen', models.BooleanField(default=False)),
                ('pets', models.BooleanField(default=False)),
                ('suitable_for_events', models.BooleanField(default=False)),
                ('smoking', models.BooleanField(default=False)),
                ('wheelchair', models.BooleanField(default=False)),
                ('elevator', models.BooleanField(default=False)),
                ('laptop_friendly', models.BooleanField(default=False)),
                ('pool', models.BooleanField(default=False)),
                ('gym', models.BooleanField(default=False)),
                ('family_friends_kids_friendly', models.BooleanField(default=False)),
                ('other_details', models.ForeignKey(default=None, to='splitnsave.products')),
            ],
        ),
        migrations.CreateModel(
            name='books',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('startdate', models.DateField()),
                ('enddate', models.DateField()),
                ('bookname', models.CharField(default=None, max_length=100)),
                ('author_first_name', models.CharField(default=0, max_length=100)),
                ('author_last_name', models.CharField(default=0, max_length=100)),
                ('sharing_type', models.CharField(default=0, max_length=100)),
                ('other_details', models.ForeignKey(default=None, to='splitnsave.products')),
            ],
        ),
        migrations.CreateModel(
            name='car_name_list',
            fields=[
                ('car_name_id', models.IntegerField(default=0, serialize=False, primary_key=True)),
                ('car_name', models.CharField(default='', max_length=100, choices=[('', ''), ('ABC', 'ABC')])),
            ],
        ),
        migrations.CreateModel(
            name='car_service_list',
            fields=[
                ('car_service_id', models.IntegerField(default=0, serialize=False, primary_key=True)),
                ('car_service', models.CharField(default='', max_length=100, choices=[('', ''), ('Uber', 'Uber')])),
            ],
        ),
        migrations.CreateModel(
            name='car_type_list',
            fields=[
                ('car_type_id', models.IntegerField(default=0, serialize=False, primary_key=True)),
                ('car_type', models.CharField(default='', max_length=100, choices=[('', ''), ('Sedan', 'Sedan')])),
            ],
        ),
        migrations.CreateModel(
            name='equipment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('startdate', models.DateField()),
                ('enddate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='keyword_list',
            fields=[
                ('keyword_id', models.IntegerField(default=0, serialize=False, primary_key=True)),
                ('keyword_name', models.CharField(default=None, max_length=100, choices=[('', ''), ('ABC', 'ABC')])),
            ],
        ),
        migrations.CreateModel(
            name='laundary',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('startdate', models.DateField()),
                ('starttime', models.TimeField()),
                ('enddate', models.DateField()),
                ('endtime', models.TimeField()),
                ('weight', models.IntegerField(default=0)),
                ('other_details', models.ForeignKey(default=None, to='splitnsave.products')),
            ],
        ),
        migrations.CreateModel(
            name='sub_category_list',
            fields=[
                ('sub_category_id', models.IntegerField(default=0, serialize=False, primary_key=True)),
                ('sub_category_name', models.CharField(default=None, max_length=100, choices=[('', ''), ('ABC', 'ABC')])),
            ],
        ),
        migrations.CreateModel(
            name='tag_list',
            fields=[
                ('tag_id', models.IntegerField(default=0, serialize=False, primary_key=True)),
                ('tag_name', models.CharField(default=None, max_length=100, choices=[('', ''), ('ABC', 'ABC')])),
            ],
        ),
        migrations.AddField(
            model_name='cabs',
            name='Music',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cabs',
            name='destination',
            field=models.CharField(default=None, max_length=1000),
        ),
        migrations.AddField(
            model_name='cabs',
            name='kids',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cabs',
            name='luggage',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cabs',
            name='non_stop_journey',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cabs',
            name='other_details',
            field=models.ForeignKey(default=None, to='splitnsave.products'),
        ),
        migrations.AddField(
            model_name='cabs',
            name='pet',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cabs',
            name='smoking',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='chat_history',
            name='delivered_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='users',
            name='verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='equipment',
            name='keyword_id1',
            field=models.ForeignKey(related_name='keyword1', to='splitnsave.keyword_list'),
        ),
        migrations.AddField(
            model_name='equipment',
            name='keyword_id2',
            field=models.ForeignKey(related_name='keyword2', to='splitnsave.keyword_list'),
        ),
        migrations.AddField(
            model_name='equipment',
            name='keyword_id3',
            field=models.ForeignKey(related_name='keyword3', to='splitnsave.keyword_list'),
        ),
        migrations.AddField(
            model_name='equipment',
            name='other_details',
            field=models.ForeignKey(default=None, to='splitnsave.products'),
        ),
        migrations.AddField(
            model_name='equipment',
            name='sub_category_id',
            field=models.ForeignKey(to='splitnsave.sub_category_list'),
        ),
        migrations.AddField(
            model_name='books',
            name='tag1',
            field=models.ForeignKey(related_name='tag1', default='', to='splitnsave.tag_list'),
        ),
        migrations.AddField(
            model_name='books',
            name='tag2',
            field=models.ForeignKey(related_name='tag2', default='', to='splitnsave.tag_list'),
        ),
        migrations.AddField(
            model_name='books',
            name='tag3',
            field=models.ForeignKey(related_name='tag3', default='', to='splitnsave.tag_list'),
        ),
        migrations.AddField(
            model_name='cabs',
            name='car_name_id',
            field=models.ForeignKey(default=None, to='splitnsave.car_name_list'),
        ),
        migrations.AddField(
            model_name='cabs',
            name='car_service_id',
            field=models.ForeignKey(default=None, to='splitnsave.car_service_list'),
        ),
        migrations.AddField(
            model_name='cabs',
            name='car_type_id',
            field=models.ForeignKey(default=None, to='splitnsave.car_type_list'),
        ),
    ]
