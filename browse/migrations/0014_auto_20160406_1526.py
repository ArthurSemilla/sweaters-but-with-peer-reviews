# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-06 15:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('browse', '0013_merge'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reviewcomment',
            options={'verbose_name_plural': 'Review Comments'},
        ),
    ]