from django.contrib import admin
from .models import MarketingCampaign
@admin.register(MarketingCampaign)
class MarketingCampaignAdmin(admin.ModelAdmin):
    list_display=("title","channel","views","replies","leads","created_at")
    list_filter=("channel","created_at")
    search_fields=("title","message")
