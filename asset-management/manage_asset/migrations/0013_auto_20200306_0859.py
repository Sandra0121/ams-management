# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2020-03-06 08:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_asset', '0012_auto_20200304_1655'),
    ]

    operations = [
        migrations.CreateModel(
            name='deleted_assets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_delete', models.CharField(max_length=1001)),
                ('itemname', models.CharField(max_length=100)),
                ('itemid', models.CharField(max_length=100)),
                ('deleted_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='lended_assets',
            name='recivername',
            field=models.CharField(max_length=100),
        ),
    ]
