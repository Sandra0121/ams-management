# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2020-03-07 18:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manage_asset', '0022_auto_20200307_1842'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lost_items',
            old_name='edited_on',
            new_name='lost_on',
        ),
    ]
