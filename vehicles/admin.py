from django.contrib import admin
from .models import Vehicle
@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display=("brand","model","year","price","status","transmission","fuel_type")
    list_filter=("status","transmission","fuel_type","year")
    search_fields=("brand","model")
