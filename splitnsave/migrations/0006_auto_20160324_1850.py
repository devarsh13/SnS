# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('splitnsave', '0005_auto_20160324_1834'),
    ]

    operations = [
        migrations.CreateModel(
            name='institute_list',
            fields=[
                ('institute_id', models.IntegerField(default=0, serialize=False, primary_key=True)),
                ('institute_name', models.CharField(default='', max_length=100, choices=[('', ''), ('DA-IICT', 'DA-IICT'), ('Nirma Institute of Technology', 'Nirma Institute of Technology')])),
            ],
        ),
        migrations.CreateModel(
            name='profession_list',
            fields=[
                ('profession_id', models.IntegerField(default=0, serialize=False, primary_key=True)),
                ('profession_name', models.CharField(default='', max_length=100, null=True, choices=[('', '')])),
            ],
        ),
        migrations.AddField(
            model_name='users',
            name='status',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='users',
            name='verification_link',
            field=models.URLField(default=None, max_length=1000),
        ),
        migrations.AlterField(
            model_name='city_list',
            name='city_name',
            field=models.CharField(default='', max_length=100, choices=[('', ''), ('Ahmedabad', 'Ahmedabad'), ('Gandhinagar', 'Gandhinagar')]),
        ),
        migrations.AddField(
            model_name='users',
            name='institute',
            field=models.ForeignKey(default=None, to='splitnsave.institute_list'),
        ),
        migrations.AddField(
            model_name='users',
            name='profession',
            field=models.ForeignKey(default=None, to='splitnsave.profession_list'),
        ),
    ]
