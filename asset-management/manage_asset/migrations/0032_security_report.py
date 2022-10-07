# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2020-07-08 18:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_asset', '0031_auto_20200326_0812'),
    ]

    operations = [
        migrations.CreateModel(
            name='security_report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=100)),
                ('detail', models.CharField(max_length=100)),
                ('reported_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
