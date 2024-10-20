# Generated by Django 5.1.1 on 2024-10-16 17:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0021_reciperequirement_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='cost',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_cost', to='Inventory.menuitem'),
        ),
    ]
