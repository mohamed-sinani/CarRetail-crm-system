from django.db import migrations,models
class Migration(migrations.Migration):
    initial=True
    dependencies = [
    ]
    operations = [
        migrations.CreateModel(
            name='MarketingCampaign',
            fields=[
                ('id',models.BigAutoField(auto_created=True,primary_key=True,serialize=False,verbose_name='ID')),
                ('title',models.CharField(max_length=140)),
                ('channel',models.CharField(choices=[('WHATSAPP_STATUS','WhatsApp Status'),('WHATSAPP_BROADCAST','WhatsApp Broadcast'),('FACEBOOK','Facebook'),('INSTAGRAM','Instagram')],max_length=30)),
                ('message',models.TextField()),
                ('whatsapp_phone',models.CharField(blank=True,help_text='Optional number for a click-to-WhatsApp link.',max_length=30)),
                ('views',models.PositiveIntegerField(default=0)),
                ('replies',models.PositiveIntegerField(default=0)),
                ('leads',models.PositiveIntegerField(default=0)),
                ('created_at',models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering':['-created_at'],
            },
        ),
    ]
