# Generated by Django 3.1.6 on 2021-04-07 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20210408_0141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_address',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_items',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_price',
            field=models.PositiveIntegerField(default=0),
        ),
    ]