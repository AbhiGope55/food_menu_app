# Generated by Django 5.1.1 on 2025-07-23 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0004_alter_item_item_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='item_image',
        ),
    ]
