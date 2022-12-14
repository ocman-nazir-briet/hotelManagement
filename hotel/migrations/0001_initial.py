# Generated by Django 4.0.6 on 2022-09-11 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=25)),
            ],
            options={
                'verbose_name_plural': 'Branch List',
            },
        ),
        migrations.CreateModel(
            name='clients',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=25)),
                ('identity', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('M', 'M'), ('F', 'F'), ('Other', 'Other')], max_length=50)),
                ('BranchName', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='hotel.branch')),
            ],
            options={
                'verbose_name_plural': 'Active Clients',
            },
        ),
        migrations.CreateModel(
            name='staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=25)),
                ('address', models.CharField(max_length=200)),
                ('category', models.CharField(choices=[('W', 'Waiter'), ('S', 'cleaning'), ('D', 'Delivery'), ('M', 'Management'), ('M', 'Manager')], max_length=1)),
                ('gender', models.CharField(choices=[('M', 'M'), ('F', 'F'), ('Other', 'Other')], max_length=50)),
                ('branchName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.branch')),
            ],
            options={
                'verbose_name_plural': 'Staff & Management',
            },
        ),
    ]
