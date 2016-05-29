# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-14 08:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email_id', models.EmailField(max_length=400)),
                ('text', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]