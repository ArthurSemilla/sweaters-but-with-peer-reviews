# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-28 00:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('browse', '0015_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peerreview',
            name='rating',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='peerreview',
            name='text',
            field=models.TextField(blank=True, max_length=100000),
        ),
    ]
