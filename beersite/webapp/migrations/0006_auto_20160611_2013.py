# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-11 20:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_auto_20160611_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cerveja',
            name='fornecedor',
            field=models.CharField(max_length=120),
        ),
    ]
