# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-17 17:29
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('browse', '0009_auto_20160211_0113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='text',
            field=models.TextField(max_length=100000, validators=[django.core.validators.MinLengthValidator(40)]),
        ),
    ]
