# Generated by Django 3.2.7 on 2021-12-22 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_rename_order_id_contact_table_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact_table',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]