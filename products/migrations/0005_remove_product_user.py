# Generated by Django 4.1.6 on 2023-02-23 04:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='user',
        ),
    ]
