# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-12 17:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0018_combinacao'),
    ]

    operations = [
        migrations.AddField(
            model_name='assinatura',
            name='cliente',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='webapp.Usuario'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='assinatura',
            name='pacote',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='webapp.Pacote'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pacote',
            name='tipo',
            field=models.ManyToManyField(to='webapp.Tipo'),
        ),
    ]