# Generated by Django 5.1.6 on 2025-03-29 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0009_order_shipped'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date_shipped',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
