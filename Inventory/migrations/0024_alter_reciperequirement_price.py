# Generated by Django 5.1.1 on 2024-10-16 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0023_alter_purchase_cost_alter_reciperequirement_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reciperequirement',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
