# Generated by Django 4.2.20 on 2025-04-23 02:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='WikiTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the tag.', max_length=255, unique=True, verbose_name='Tag Name')),
            ],
        ),
        migrations.CreateModel(
            name='WikiArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Path to the article, e.g. /wiki/what-is-django/', max_length=255, verbose_name='title')),
                ('grub', models.CharField(help_text='Grub is a unique identifier for the article, used in the URL.', max_length=255, unique=True, verbose_name='Grub')),
                ('content', models.TextField(blank=True, default='', help_text='Content of the article, supports Markdown.', verbose_name='Content')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date and time when the article was created.', verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date and time when the article was last updated.', verbose_name='Updated At')),
                ('author', models.ForeignKey(help_text='Author of the article.', on_delete=django.db.models.deletion.PROTECT, related_name='articles', to=settings.AUTH_USER_MODEL, verbose_name='Author')),
                ('parent', models.ForeignKey(blank=True, default=None, help_text='Parent article for nested articles.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='wiki.wikiarticle', verbose_name='Parent Article')),
                ('tags', models.ManyToManyField(blank=True, default=None, help_text='Tags associated with the article.', related_name='articles', to='wiki.wikitag', verbose_name='Tags')),
            ],
        ),
    ]
