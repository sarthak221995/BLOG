# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-24 03:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_auto_20160323_1838'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='tags',
        ),
        migrations.DeleteModel(
            name='taggie',
        ),
    ]