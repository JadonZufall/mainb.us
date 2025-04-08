from django.contrib import admin
import apps.filestore.models as models

# Register your models here.


@admin.register(models.File)
class FileAdmin(admin.ModelAdmin):
	pass

