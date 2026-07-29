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
    link_url = models.CharField(
        max_length=200,
        blank=True,
        help_text="For WhatsApp: phone number (e.g. 2557XXXXXXXX). For Instagram/Facebook: full URL.",
    )
    views=models.PositiveIntegerField(default=0)
    replies=models.PositiveIntegerField(default=0)
    leads=models.PositiveIntegerField(default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering=["-created_at"]
    def __str__(self):
        return self.title
