from django.contrib import admin

import apps.authentication.models as models


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
	list_display = ["username", "is_superuser",]
	filter_horizontal = ("groups",)

@admin.register(models.Group)
class GroupAdmin(admin.ModelAdmin):
	list_display = ["name", "desc",]
	filter_horizontal = ("permissions",)

@admin.register(models.Permission)
class PermissionAdmin(admin.ModelAdmin):
	list_display = ["code", "name", "desc",]
