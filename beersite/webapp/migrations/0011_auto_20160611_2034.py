# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-11 20:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0010_remove_cerveja_timestamp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cerveja',
            name='quantidadeNoPacote',
        ),
        migrations.AlterField(
            model_name='cerveja',
            name='fornecedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.Fornecedor'),
        ),
    ]
