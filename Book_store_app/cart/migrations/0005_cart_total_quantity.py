# Generated by Django 4.1.2 on 2022-10-11 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_rename_book_id_cartitem_book_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='total_quantity',
            field=models.IntegerField(default=0),
        ),
    ]
