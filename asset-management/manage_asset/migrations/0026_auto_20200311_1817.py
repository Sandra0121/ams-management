# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2020-03-11 18:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_asset', '0025_auto_20200311_0759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nonassets',
            name='is_assigned',
            field=models.BooleanField(default=False),
        ),
    ]