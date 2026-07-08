fromdjango.contribimportadmin
from.modelsimportReportSnapshot
@admin.register(ReportSnapshot)
classReportSnapshotAdmin(admin.ModelAdmin):
    list_display=("title","report_type","generated_at")
    list_filter=("report_type",)
