# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2020-03-07 10:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('manage_asset', '0019_auto_20200306_1034'),
    ]

    operations = [
        migrations.AddField(
            model_name='nonassets',
            name='updated_on',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
