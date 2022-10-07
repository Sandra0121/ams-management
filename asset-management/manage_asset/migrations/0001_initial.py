# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-11-28 14:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='conassets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coname', models.CharField(max_length=40)),
                ('coqunty', models.CharField(max_length=40)),
                ('colocation', models.CharField(max_length=40)),
                ('cocategory', models.CharField(max_length=40)),
                ('costatus', models.CharField(max_length=40)),
                ('codescrp', models.CharField(max_length=200)),
                ('unitt', models.CharField(max_length=40)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='nonassets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nocname', models.CharField(max_length=100)),
                ('nocid', models.CharField(max_length=40)),
                ('nocdescp', models.CharField(max_length=200)),
                ('noclocation', models.CharField(max_length=40)),
                ('noccategory', models.CharField(max_length=40)),
                ('nocstatus', models.CharField(max_length=40)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
