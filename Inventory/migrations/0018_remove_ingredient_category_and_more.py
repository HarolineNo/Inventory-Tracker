# Generated by Django 5.1.1 on 2024-10-16 03:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0017_ingredient_date_purchased_ingredient_expiration_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='category',
        ),
        migrations.RemoveField(
            model_name='ingredient',
            name='date_purchased',
        ),
        migrations.RemoveField(
            model_name='ingredient',
            name='expiration_date',
        ),
    ]
