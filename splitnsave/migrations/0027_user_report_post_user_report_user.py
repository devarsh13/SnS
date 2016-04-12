# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('splitnsave', '0026_auto_20160412_1703'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_report_post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.IntegerField(default=0)),
                ('product_id', models.ForeignKey(to='splitnsave.products')),
                ('user_id', models.ForeignKey(to='splitnsave.users')),
            ],
        ),
        migrations.CreateModel(
            name='user_report_user',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.IntegerField(default=0)),
                ('user1', models.ForeignKey(related_name='user1', to='splitnsave.users')),
                ('user2', models.ForeignKey(related_name='user2', to='splitnsave.users')),
            ],
        ),
    ]
