# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-12 01:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0013_cerveja_foto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='combinacao',
            name='status',
        ),
        migrations.AddField(
            model_name='combinacao',
            name='ativo',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='combinacao',
            name='cervejas',
            field=models.ManyToManyField(to='webapp.Cerveja'),
        ),
        migrations.AddField(
            model_name='combinacao',
            name='pacote',
            field=models.ForeignKey(default='null', on_delete=django.db.models.deletion.CASCADE, to='webapp.Pacote'),
        ),
    ]