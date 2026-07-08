fromdjango.contribimportadmin
from.modelsimportAnnouncement
@admin.register(Announcement)
classAnnouncementAdmin(admin.ModelAdmin):
    list_display=("title","created_by","created_at")
    search_fields=("title","message")
