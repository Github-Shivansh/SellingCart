# Generated by Django 3.0.4 on 2020-05-06 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_auto_20200505_0731'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=40)),
                ('address1', models.CharField(max_length=800)),
                ('address2', models.CharField(max_length=800)),
                ('city', models.CharField(max_length=100)),
                ('mobile_no', models.IntegerField()),
                ('dilevery_mode', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=10)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Product')),
            ],
        ),
    ]
