# Generated by Django 3.0.7 on 2020-11-19 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ztx', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='costomer',
            name='money',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='余额'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='价格'),
        ),
    ]
