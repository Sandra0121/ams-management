# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-12-10 16:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_asset', '0010_lended_assets'),
    ]

    operations = [
        migrations.AddField(
            model_name='lended_assets',
            name='recivername',
            field=models.CharField(default='jack', max_length=1001),
        ),
    ]
