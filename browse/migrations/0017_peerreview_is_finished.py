# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-04 23:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('browse', '0016_auto_20160428_0048'),
    ]

    operations = [
        migrations.AddField(
            model_name='peerreview',
            name='is_finished',
            field=models.BooleanField(default=False),
        ),
    ]
