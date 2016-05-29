# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-23 09:44
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20160323_1300'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='draft',
            field=models.BooleanField(default='False'),
        ),
        migrations.AddField(
            model_name='post',
            name='publish',
            field=models.DateField(default=datetime.datetime(2016, 3, 23, 9, 44, 26, 895870, tzinfo=utc)),
            preserve_default=False,
        ),
    ]