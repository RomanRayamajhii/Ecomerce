# Generated by Django 5.1.6 on 2025-03-26 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0004_order_orderitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippingaddress',
            name='shipping_phonenumber',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='shipping_zipcode',
            field=models.CharField(default='', max_length=200),
        ),
    ]
