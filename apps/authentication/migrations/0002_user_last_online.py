# Generated by Django 5.2 on 2025-04-16 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='last_online',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]
