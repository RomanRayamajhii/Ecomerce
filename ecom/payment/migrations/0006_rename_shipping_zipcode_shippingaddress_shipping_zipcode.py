# Generated by Django 5.1.6 on 2025-03-26 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0005_shippingaddress_shipping_phonenumber_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='shipping_zipcode',
            new_name='shipping_zipCode',
        ),
    ]
