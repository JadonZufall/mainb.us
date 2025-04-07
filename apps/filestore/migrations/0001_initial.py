# Generated by Django 5.1.7 on 2025-04-07 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=500)),
                ('slug', models.SlugField(unique=True)),
                ('videofile', models.FileField(null=True, upload_to='media/')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('date_altered', models.DateTimeField(auto_now=True, verbose_name='Date Altered')),
            ],
            options={
                'ordering': ['-date_created'],
            },
        ),
    ]
