# Generated by Django 3.2.7 on 2021-12-26 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_delete_contact_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact_table',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(default=' ', max_length=122)),
                ('email', models.CharField(max_length=122)),
                ('phone', models.CharField(max_length=122)),
                ('decs', models.TextField(max_length=122)),
                ('date', models.DateField()),
            ],
        ),
    ]
