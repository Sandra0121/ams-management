# Generated by Django 3.2.15 on 2022-08-27 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_asset', '0040_alter_asset_auto_tracking_reader_loc'),
    ]

    operations = [
        migrations.AddField(
            model_name='nonassets',
            name='tag_id',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='nonassets',
            name='nocid',
            field=models.CharField(max_length=40, unique=True),
        ),
    ]
