# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2020-03-11 07:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_asset', '0023_auto_20200307_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='costatus',
            field=models.BooleanField(default=True),
        ),
    ]
