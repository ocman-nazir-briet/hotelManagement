# Generated by Django 4.0.6 on 2022-09-13 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0011_alter_orders_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='clients',
            name='roomNo',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
