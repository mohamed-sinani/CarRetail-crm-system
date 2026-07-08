from django.contrib import admin
from .models import Customer
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display=("full_name","phone","email","assigned_salesperson")
    search_fields=("full_name","phone","email")
    list_filter=("assigned_salesperson",)
