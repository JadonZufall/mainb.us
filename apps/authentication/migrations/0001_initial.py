# Generated by Django 4.2.20 on 2025-04-23 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('code', models.SlugField(unique=True)),
                ('desc', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('desc', models.TextField(blank=True, null=True)),
                ('permissions', models.ManyToManyField(blank=True, to='authentication.permission')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=32, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_locked', models.BooleanField(default=False)),
                ('is_tester', models.BooleanField(default=False)),
                ('is_bot', models.BooleanField(default=False)),
                ('is_fixture', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_altered', models.DateTimeField(auto_now=True)),
                ('last_online', models.DateTimeField(default=None, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to.', related_name='user_set', to='authentication.group', verbose_name='groups')),
                ('permissions', models.ManyToManyField(blank=True, help_text='The permissions this user holds.', related_name='permissions_set', to='authentication.permission', verbose_name='permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
