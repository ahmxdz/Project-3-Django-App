# Generated by Django 4.0.3 on 2022-04-09 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_stock_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='num_of_units',
            field=models.IntegerField(verbose_name='# of Units'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='purchase_price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Purchase Price'),
        ),
    ]
