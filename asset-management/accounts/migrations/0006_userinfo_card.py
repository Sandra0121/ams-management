# Generated by Django 3.2.15 on 2022-09-13 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20200319_1813'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='card',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
