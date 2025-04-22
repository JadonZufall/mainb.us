from django.contrib import admin

from apps.vmdash import models


@admin.register(models.VehicleManufacturer)
class VehicleManufacturerAdmin(admin.ModelAdmin):
	pass

@admin.register(models.VehicleMake)
class VehicleMakeAdmin(admin.ModelAdmin):
	pass

@admin.register(models.VehicleModel)
class VehicleModelAdmin(admin.ModelAdmin):
	pass

@admin.register(models.VehicleMaintenanceType)
class VehicleMaintenanceTypeAdmin(admin.ModelAdmin):
	pass

@admin.register(models.VehicleMaintenanceRecord)
class VehicleMaintenanceRecordAdmin(admin.ModelAdmin):
	pass


@admin.register(models.Vehicle)
class VehicleAdmin(admin.ModelAdmin):
	pass