# Generated by Django 4.0.6 on 2022-09-12 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0002_food_clients_fooditems'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='price',
            field=models.CharField(max_length=10),
        ),
    ]
