# Generated by Django 4.0.6 on 2022-09-13 08:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0008_remove_order_ordereditems_order_ordereditems'),
    ]

    operations = [
        migrations.CreateModel(
            name='order2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='hotel.clients')),
                ('orderedItems', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.food')),
            ],
            options={
                'verbose_name_plural': 'Orders',
            },
        ),
        migrations.DeleteModel(
            name='order',
        ),
    ]
