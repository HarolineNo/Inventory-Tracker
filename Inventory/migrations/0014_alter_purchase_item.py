# Generated by Django 5.1.1 on 2024-10-16 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0013_alter_ingredient_name_alter_purchase_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='item',
            field=models.CharField(max_length=50),
        ),
    ]