# Generated by Django 5.2 on 2025-04-19 02:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MaintenanceRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('miles', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MaintenanceTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_repeat', models.DurationField(default=None, help_text='Repeat every x time passed sense this maintance was last performed.', null=True, verbose_name='Time Repeat')),
                ('mile_repeat', models.IntegerField(default=None, help_text='Repeat every time the car has passed x miles.', null=True, verbose_name='Mile Repeat')),
                ('records', models.ManyToManyField(to='vmdash.maintenancerecord')),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=64, null=True, verbose_name='Name')),
                ('make', models.CharField(max_length=64, verbose_name='Make')),
                ('model', models.CharField(max_length=64, verbose_name='Model')),
                ('year', models.IntegerField(verbose_name='Year')),
                ('plate', models.CharField(verbose_name='Plate')),
                ('vin', models.CharField(verbose_name='VIN')),
                ('miles', models.IntegerField(help_text='The miles that are on the car', verbose_name='Miles')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owned_by', to=settings.AUTH_USER_MODEL)),
                ('maintenance', models.ManyToManyField(to='vmdash.maintenancetypes')),
            ],
        ),
    ]
