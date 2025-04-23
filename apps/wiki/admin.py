from django.contrib import admin
from apps.wiki.models import WikiArticle


@admin.register(WikiArticle)
class WikiPageAdmin(admin.ModelAdmin):
	pass