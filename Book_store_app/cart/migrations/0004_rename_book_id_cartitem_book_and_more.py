# Generated by Django 4.1 on 2022-10-11 03:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_rename_user_id_cartitem_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='book_id',
            new_name='book',
        ),
        migrations.RenameField(
            model_name='cartitem',
            old_name='cart_id',
            new_name='cart',
        ),
    ]
