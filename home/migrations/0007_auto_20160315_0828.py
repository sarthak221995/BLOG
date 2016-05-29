# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-15 02:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_post_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='tags',
        ),
        migrations.AddField(
            model_name='post',
            name='featured',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]