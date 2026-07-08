fromdjango.contribimportadmin
fromdjango.contrib.auth.adminimportUserAdmin
from.modelsimportUser
@admin.register(User)
classCRMUserAdmin(UserAdmin):
    fieldsets=UserAdmin.fieldsets+(("CRM Profile",{"fields":("role","phone")}),)
    list_display=("username","email","role","is_staff","is_active")
    list_filter=("role","is_staff","is_active")
