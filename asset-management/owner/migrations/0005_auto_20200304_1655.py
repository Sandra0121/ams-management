# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2020-03-04 16:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0004_auto_20200223_0909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requested_assets',
            name='request_status',
            field=models.IntegerField(),
        ),
    ]
