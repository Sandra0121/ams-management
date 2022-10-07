# Generated by Django 3.2.15 on 2022-08-30 13:57

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('manage_asset', '0041_auto_20220827_1619'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nonassets',
            name='id',
        ),
        migrations.AlterField(
            model_name='nonassets',
            name='nocid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]