# Generated by Django 3.1 on 2023-04-16 07:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_auto_20230413_1511'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order_product',
            name='color',
        ),
        migrations.RemoveField(
            model_name='order_product',
            name='size',
        ),
    ]