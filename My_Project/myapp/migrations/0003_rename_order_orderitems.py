# Generated by Django 5.0.4 on 2024-05-20 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_products_orders_order'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Order',
            new_name='OrderItems',
        ),
    ]