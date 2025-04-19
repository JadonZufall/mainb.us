# Generated by Django 5.2 on 2025-04-19 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vmdash', '0002_rename_maintenancetypes_maintenancetype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='maintenance',
            field=models.ManyToManyField(blank=True, to='vmdash.maintenancetype'),
        ),
        migrations.AlterField(
            model_name='car',
            name='miles',
            field=models.IntegerField(blank=True, help_text='The miles that are on the car', verbose_name='Miles'),
        ),
        migrations.AlterField(
            model_name='car',
            name='plate',
            field=models.CharField(blank=True, verbose_name='Plate'),
        ),
        migrations.AlterField(
            model_name='car',
            name='vin',
            field=models.CharField(blank=True, verbose_name='VIN'),
        ),
    ]
