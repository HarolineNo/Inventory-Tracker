# Generated by Django 5.1.1 on 2024-09-30 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0002_rename_ingredients_ingredient_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='cost',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
