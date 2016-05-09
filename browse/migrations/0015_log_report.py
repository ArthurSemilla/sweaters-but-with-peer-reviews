# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-20 16:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('browse', '0014_auto_20160413_2125'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target_serialized', models.TextField(max_length=1000, null=True)),
                ('action', models.TextField(max_length=10000, null=True)),
                ('comment', models.TextField(max_length=10000, null=True)),
                ('created_ts', models.DateTimeField(auto_now_add=True)),
                ('updated_ts', models.DateTimeField(auto_now=True)),
                ('category', models.CharField(choices=[('add', 'Add'), ('del', 'Delete'), ('mod', 'Modify'), ('rep', 'Report'), ('han', 'Report Resolution'), ('oth', 'Other')], default='oth', max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('handled_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='handled_by', to='browse.Log')),
                ('target_log', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='target_log', to='browse.Log')),
            ],
        ),
    ]
