# Generated by Django 4.2.7 on 2024-03-24 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_alter_products_name'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='categories',
            table='category',
        ),
        migrations.AlterModelTable(
            name='products',
            table='product',
        ),
    ]
