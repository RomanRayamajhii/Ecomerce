# Generated by Django 5.1.6 on 2025-03-22 03:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='Address',
            new_name='shipping_Address',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='city',
            new_name='shipping_city',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='country',
            new_name='shipping_country',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='district',
            new_name='shipping_district',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='full_name',
            new_name='shipping_state',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='state',
            new_name='shippingfull_name',
        ),
    ]
