from django.contrib import admin
from .models import ReportSnapshot
@admin.register(ReportSnapshot)
class ReportSnapshotAdmin(admin.ModelAdmin):
    list_display=("title","report_type","generated_at")
    list_filter=("report_type",)
