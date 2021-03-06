# Generated by Django 3.0.4 on 2020-04-17 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_cartitems_item_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.CharField(max_length=1000)),
                ('item_Quantity', models.IntegerField(default=0)),
                ('customer_name', models.CharField(max_length=40)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.Product')),
            ],
        ),
        migrations.DeleteModel(
            name='CartItems',
        ),
    ]
