# Generated by Django 5.1.1 on 2024-09-30 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0006_alter_reciperequirement_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reciperequirement',
            name='quantity',
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
    ]
