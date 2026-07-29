from django.test import TestCase
from .models import MarketingCampaign

class MarketingCampaignModelTest(TestCase):
    def test_create_campaign(self):
        c=MarketingCampaign.objects.create(title="Summer Sale",channel=MarketingCampaign.Channel.FACEBOOK,message="Big discounts!")
        self.assertEqual(str(c),"Summer Sale")
        self.assertEqual(c.channel,"FACEBOOK")
        self.assertEqual(c.views,0)
