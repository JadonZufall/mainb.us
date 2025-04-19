from django.contrib import admin

from apps.vmdash import models


@admin.register(models.Car)
class CarAdmin(admin.ModelAdmin):
	pass

@admin.register(models.MaintenanceType)
class MaintenanceTypeAdmin(admin.ModelAdmin):
	pass

@admin.register(models.MaintenanceRecord)
class MaintenanceRecordAdmin(admin.ModelAdmin):
	pass