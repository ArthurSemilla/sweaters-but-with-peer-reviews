# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-02 20:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('browse', '0017_log_created_by'),
    ]

    operations = [
        migrations.RenameField(
            model_name='log',
            old_name='created_by',
            new_name='owner',
        ),
    ]