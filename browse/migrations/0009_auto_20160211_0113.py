# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-11 01:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('browse', '0008_auto_20160206_0307'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='source',
            new_name='owner',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='professor',
            new_name='target',
        ),
        migrations.RenameField(
            model_name='reviewvote',
            old_name='reviewer',
            new_name='owner',
        ),
        migrations.RenameField(
            model_name='reviewvote',
            old_name='review',
            new_name='target',
        ),
        migrations.AlterField(
            model_name='reviewvote',
            name='quality',
            field=models.BooleanField(),
        ),
    ]
