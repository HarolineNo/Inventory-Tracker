# Generated by Django 5.1.1 on 2024-10-16 18:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0025_alter_purchase_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='ingredient',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='purchased_ingredient', to='Inventory.reciperequirement'),
        ),
    ]
