# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-21 21:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='video',
            unique_together=set([('youtube_url', 'youtube_url')]),
        ),
    ]