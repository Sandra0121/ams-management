# Generated by Django 3.2.15 on 2022-09-13 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_asset', '0060_auto_20220913_2148'),
    ]

    operations = [
        migrations.AddField(
            model_name='authorization',
            name='username',
            field=models.CharField(default='User1', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='authorization',
            name='cid',
            field=models.CharField(max_length=100),
        ),
    ]