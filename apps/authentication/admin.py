from django import forms
from django.contrib import admin

import apps.authentication.models as models


class UserAdminForm(forms.ModelForm):
	class Meta:
		model = models.User
		fields = "__all__"
	
	def __init__(self, *args, **kwargs) -> None:
		super().__init__(*args, **kwargs)
		for key, value in self.fields.items():
			if isinstance(value, forms.fields.BooleanField):
				print(key)
				value.widget.attrs.update({"class": "inline-boolean"})


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
	form = UserAdminForm

	list_display = [
		"username", "is_active", "is_staff", "is_superuser",
	]
	ordering = [
		"username",
	]

	search_fields = [
		"username",
	]
	readonly_fields = [
		"password", "date_created", "date_altered", "last_login",
	]
	filter_horizontal = [
		"groups",
		"permissions",
	]
	filter_vertical = [

	]
	
	fieldsets = [
		["Account", {
			"fields": ["username", "password",],
		}],
		["Options", {
			"fields": ["is_active", "is_staff", "is_superuser",],
		}],
		["Metadata", {
			"fields": ["date_created", "date_altered", "last_login",],
		}],
		["Groups", {
			"fields": ["groups",],
		}],
		["Permissions", {
			"fields": ["permissions",],
		}],
	]

	class Media:
		css = {
			"all": ["admin/css/custom.css",],
		}

@admin.register(models.Group)
class GroupAdmin(admin.ModelAdmin):
	list_display = ["name", "desc",]
	filter_horizontal = ["permissions",]

@admin.register(models.Permission)
class PermissionAdmin(admin.ModelAdmin):
	list_display = ["code", "name", "desc",]
