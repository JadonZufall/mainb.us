from django.contrib import admin
import apps.filestore.models as models

# Register your models here.


@admin.register(models.File)
class FileAdmin(admin.ModelAdmin):
	list_display = ["name", "file", "filetype", "views", "downloads", "author"]
	readonly_fields = ["author", "views", "downloads", "filetype", "file" "date_created", "date_altered",]

	class Meta:
		ordering = ["-date_created"]

