# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-10-30 05:09
from __future__ import unicode_literals

import ckeditor.fields
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
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('author', models.CharField(blank=True, max_length=400, null=True)),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('featured', models.BooleanField(default='False')),
                ('draft', models.BooleanField(default='False')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_tag', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='tag_field',
            field=models.ManyToManyField(to='home.Tag'),
        ),
    ]
