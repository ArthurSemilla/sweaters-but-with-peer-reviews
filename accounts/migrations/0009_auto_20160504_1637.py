# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-04 16:37
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20160428_0048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='timezone',
            field=models.CharField(default=datetime.datetime(2016, 5, 4, 16, 37, 32, 549756, tzinfo=utc), max_length=100),
        ),
    ]