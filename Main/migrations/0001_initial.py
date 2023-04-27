# Generated by Django 4.1 on 2023-04-27 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Vendor', '__first__'),
        ('Authapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('cart_id', models.AutoField(primary_key=True, serialize=False)),
                ('is_paid', models.BooleanField(default=False)),
                ('cust_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Authapp.customers')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('contact_id', models.AutoField(primary_key=True, serialize=False)),
                ('contact_name', models.CharField(max_length=100)),
                ('contact_email', models.EmailField(max_length=254)),
                ('contact_message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CartItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.cart')),
                ('game', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Vendor.games')),
            ],
        ),
    ]
