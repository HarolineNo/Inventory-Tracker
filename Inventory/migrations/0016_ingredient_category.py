# Generated by Django 5.1.1 on 2024-10-16 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0015_alter_purchase_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='category',
            field=models.CharField(default=None, max_length=200),
        ),
    ]