# Generated by Django 5.1.1 on 2024-10-16 19:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0031_alter_purchase_ingredient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='ingredient',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='purchased_ingredient', to='Inventory.ingredient'),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.menuitem'),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='quantity',
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='unit_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
