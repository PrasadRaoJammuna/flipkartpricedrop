# Generated by Django 2.2.6 on 2019-11-11 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flipkart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricedrop',
            name='curr_price',
            field=models.DecimalField(decimal_places=2, max_digits=10000),
        ),
    ]
