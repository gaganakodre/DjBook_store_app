# Generated by Django 4.1.2 on 2022-10-10 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_rename_quantiy_cartitem_quantity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='user_id',
            new_name='user',
        ),
    ]
