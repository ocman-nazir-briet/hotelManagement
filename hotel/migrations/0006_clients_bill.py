# Generated by Django 4.0.6 on 2022-09-12 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0005_alter_clients_gender_alter_clients_identity'),
    ]

    operations = [
        migrations.AddField(
            model_name='clients',
            name='bill',
            field=models.CharField(choices=[('Paid', 'Paid'), ('Pending', 'Pending'), ('Cancelled', 'Cancelled')], default='Pending', max_length=50),
        ),
    ]
