from django.contrib import admin
from .models import Deal
@admin.register(Deal)
class DealAdmin(admin.ModelAdmin):
    list_display=("customer","vehicle","salesperson","stage","expected_value","updated_at")
    list_filter=("stage","salesperson")
    search_fields=("customer__full_name","vehicle__brand","vehicle__model")
