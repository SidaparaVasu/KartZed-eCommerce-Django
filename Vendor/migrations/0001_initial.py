# Generated by Django 4.1 on 2023-04-25 12:02

import Vendor.models
from django.db import migrations, models
import django.db.models.deletion
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Authapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Games',
            fields=[
                ('gid', models.AutoField(primary_key=True, serialize=False)),
                ('product_key', models.CharField(max_length=16, unique=True)),
                ('game_logo', models.ImageField(blank=True, null=True, upload_to=Vendor.models.game_logo_filepath)),
                ('game_name', models.CharField(max_length=25)),
                ('game_description', models.CharField(max_length=300)),
                ('game_developer', models.CharField(max_length=25)),
                ('game_publisher', models.CharField(max_length=25)),
                ('game_storage', models.CharField(max_length=6)),
                ('game_ram', models.CharField(max_length=3)),
                ('game_languages', models.CharField(max_length=25)),
                ('game_release_date', models.CharField(max_length=6)),
                ('game_price', models.IntegerField()),
                ('avail_stock', models.IntegerField()),
                ('discount', models.CharField(max_length=3)),
                ('game_images', models.ImageField(blank=True, null=True, upload_to=Vendor.models.game_image_filepath)),
                ('game_features', djongo.models.fields.JSONField(default=list)),
                ('game_modes', djongo.models.fields.JSONField(default=list)),
                ('game_categories', djongo.models.fields.JSONField(default=list)),
                ('platform_names', djongo.models.fields.JSONField(default=list)),
                ('os_names', models.CharField(max_length=100)),
                ('os_versions', models.CharField(max_length=100)),
                ('processors_names', models.CharField(max_length=100)),
                ('vc_names', models.CharField(max_length=100)),
                ('vc_versions', models.CharField(max_length=100)),
                ('vendor_reference', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Authapp.vendors')),
            ],
        ),
    ]
