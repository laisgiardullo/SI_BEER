# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-11 20:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_cerveja_timestamp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cerveja',
            name='timestamp',
        ),
    ]
