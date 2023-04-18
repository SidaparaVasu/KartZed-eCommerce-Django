# Generated by Django 4.1 on 2023-04-18 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=6)),
                ('email_id', models.CharField(max_length=320, unique=True)),
                ('password', models.CharField(max_length=12)),
                ('phone_number', models.CharField(max_length=10, unique=True)),
                ('is_phone_verified', models.BooleanField(default=False)),
                ('otp', models.CharField(max_length=6)),
                ('user_type', models.CharField(max_length=9)),
            ],
            options={
                'db_table': 'Main_Users',
            },
        ),
    ]
