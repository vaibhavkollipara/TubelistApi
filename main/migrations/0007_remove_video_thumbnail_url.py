# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-27 01:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20170423_1447'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='thumbnail_url',
        ),
    ]
