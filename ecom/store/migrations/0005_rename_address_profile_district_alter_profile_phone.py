# Generated by Django 5.1.6 on 2025-03-12 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_profile_date_modified'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='address',
            new_name='district',
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(max_length=10),
        ),
    ]
