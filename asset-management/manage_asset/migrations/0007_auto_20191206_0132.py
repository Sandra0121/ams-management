# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-12-06 01:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_asset', '0006_assigned_assets'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nonassets',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
