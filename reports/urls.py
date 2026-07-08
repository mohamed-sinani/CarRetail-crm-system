from django.urls import path
from .import views
app_name="reports"
urlpatterns = [
    path("",views.report_center,name="list"),
    path("export/<str:kind>/<str:fmt>/",views.export_report,name="export"),
]
