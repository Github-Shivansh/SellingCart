# Generated by Django 3.0.4 on 2020-05-05 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_remove_cartitem_item_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='item_quantity',
            field=models.IntegerField(default=1),
        ),
    ]
