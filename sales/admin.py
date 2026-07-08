fromdjango.contribimportadmin
from.modelsimportSale
@admin.register(Sale)
classSaleAdmin(admin.ModelAdmin):
    list_display=("vehicle","customer","salesperson","amount","payment_method","sale_date")
    list_filter=("payment_method","sale_date","salesperson")
    search_fields=("vehicle__brand","vehicle__model","customer__full_name")
