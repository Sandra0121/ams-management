# Generated by Django 3.2.4 on 2021-06-28 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manage_asset', '0033_remove_security_report_day'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asset_auto_tracking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reader_loc', models.CharField(max_length=50)),
                ('read_at', models.DateTimeField(auto_now_add=True)),
                ('asset_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manage_asset.nonassets')),
            ],
        ),
    ]