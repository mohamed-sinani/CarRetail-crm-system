from django.db import models
class MarketingCampaign(models.Model):
    class Channel(models.TextChoices):
        WHATSAPP_STATUS="WHATSAPP_STATUS","WhatsApp Status"
        WHATSAPP_BROADCAST="WHATSAPP_BROADCAST","WhatsApp Broadcast"
        FACEBOOK="FACEBOOK","Facebook"
        INSTAGRAM="INSTAGRAM","Instagram"
    title=models.CharField(max_length=140)
    channel=models.CharField(max_length=30,choices=Channel.choices)
    message=models.TextField()
    whatsapp_phone = models.CharField(
        max_length=30,
        blank=True,
        help_text="Optional number for a click-to-WhatsApp link.",
    )
    views=models.PositiveIntegerField(default=0)
    replies=models.PositiveIntegerField(default=0)
    leads=models.PositiveIntegerField(default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering=["-created_at"]
    def __str__(self):
        returnself.title
