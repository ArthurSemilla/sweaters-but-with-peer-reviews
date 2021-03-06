# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-03 20:24
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('browse', '0003_auto_20160203_2007'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='url',
            field=models.CharField(blank=True, max_length=100, null=True, validators=[django.core.validators.URLValidator]),
        ),
        migrations.AddField(
            model_name='school',
            name='url',
            field=models.CharField(blank=True, max_length=100, null=True, validators=[django.core.validators.URLValidator]),
        ),
        migrations.AlterField(
            model_name='school',
            name='email_pattern',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator]),
        ),
    ]
