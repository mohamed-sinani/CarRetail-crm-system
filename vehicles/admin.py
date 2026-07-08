fromdjango.contribimportadmin
from.modelsimportVehicle
@admin.register(Vehicle)
classVehicleAdmin(admin.ModelAdmin):
    list_display=("brand","model","year","price","status","transmission","fuel_type")
    list_filter=("status","transmission","fuel_type","year")
    search_fields=("brand","model")
