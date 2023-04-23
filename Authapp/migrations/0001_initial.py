# Generated by Django 4.1 on 2023-04-23 07:36

import Authapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admins',
            fields=[
                ('admin_id', models.AutoField(primary_key=True, serialize=False)),
                ('admin_name', models.CharField(max_length=20)),
                ('admin_role', models.CharField(max_length=40)),
                ('admin_email', models.CharField(max_length=20)),
                ('admin_password', models.CharField(max_length=12)),
                ('admin_image', models.ImageField(blank=True, null=True, upload_to=Authapp.models.filepath)),
            ],
        ),
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('cust_id', models.AutoField(primary_key=True, serialize=False)),
                ('cust_first_name', models.CharField(max_length=20)),
                ('cust_last_name', models.CharField(max_length=20)),
                ('cust_gender', models.CharField(max_length=6)),
                ('cust_email', models.CharField(max_length=20)),
                ('cust_phone_number', models.CharField(max_length=13)),
                ('is_phone_verified', models.BooleanField(default=False)),
                ('otp', models.CharField(max_length=6)),
                ('cust_country', models.CharField(max_length=25)),
                ('cust_state', models.CharField(max_length=25)),
                ('cust_city', models.CharField(max_length=25)),
                ('cust_address', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Vendors',
            fields=[
                ('vendor_id', models.AutoField(primary_key=True, serialize=False)),
                ('vendor_fullname', models.CharField(max_length=20)),
                ('vendor_password', models.CharField(max_length=12)),
                ('vendor_email', models.CharField(max_length=20, unique=True)),
                ('vendor_phone_number', models.CharField(max_length=10, unique=True)),
                ('company_name', models.CharField(max_length=30, unique=True)),
                ('company_address', models.CharField(max_length=50)),
                ('company_phone_number', models.CharField(max_length=10, unique=True)),
                ('GSTIN', models.CharField(max_length=15, unique=True)),
                ('pickup_pincode', models.CharField(max_length=10)),
                ('pickup_address', models.CharField(max_length=50)),
            ],
        ),
    ]
