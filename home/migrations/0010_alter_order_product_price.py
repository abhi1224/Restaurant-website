# Generated by Django 3.2.7 on 2021-12-22 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20211221_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='product_price',
            field=models.CharField(max_length=122),
        ),
    ]