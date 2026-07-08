fromdjango.contribimportadmin
from.modelsimportCustomer
@admin.register(Customer)
classCustomerAdmin(admin.ModelAdmin):
    list_display=("full_name","phone","email","assigned_salesperson")
    search_fields=("full_name","phone","email")
    list_filter=("assigned_salesperson",)
