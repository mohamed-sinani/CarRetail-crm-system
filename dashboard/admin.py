fromdjango.contribimportadmin
from.modelsimportMarketingCampaign
@admin.register(MarketingCampaign)
classMarketingCampaignAdmin(admin.ModelAdmin):
    list_display=("title","channel","views","replies","leads","created_at")
    list_filter=("channel","created_at")
    search_fields=("title","message")
