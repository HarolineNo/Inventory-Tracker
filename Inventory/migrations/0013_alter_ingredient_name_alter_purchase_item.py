# Generated by Django 5.1.1 on 2024-10-16 02:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0012_alter_reciperequirement_ingredient_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.menuitem'),
        ),
    ]