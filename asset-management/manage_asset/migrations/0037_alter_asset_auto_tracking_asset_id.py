# Generated by Django 3.2.4 on 2021-06-28 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_asset', '0036_alter_asset_auto_tracking_asset_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset_auto_tracking',
            name='asset_id',
            field=models.TextField(),
        ),
    ]
