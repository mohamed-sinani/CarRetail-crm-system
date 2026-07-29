from django import forms
from .models import MarketingCampaign
class MarketingCampaignForm(forms.ModelForm):
    class Meta:
        model=MarketingCampaign
        fields=["title","channel","message","whatsapp_phone","views","replies","leads"]
        widgets = {
            "title":forms.TextInput(attrs={"class":"form-control","placeholder":"Weekend SUV Showcase","maxlength":"140"}),
            "channel":forms.Select(attrs={"class":"form-select"}),
            "message": forms.Textarea(
                attrs={
                    "class":"form-control",
                    "rows":5,
                    "placeholder":"Write the promotion text staff will copy to WhatsApp Status, broadcast, Facebook, or Instagram.",
                }
            ),
            "whatsapp_phone":forms.TextInput(attrs={"class":"form-control","placeholder":"255XXXXXXXXX"}),
            "views":forms.NumberInput(attrs={"class":"form-control","min":0}),
            "replies":forms.NumberInput(attrs={"class":"form-control","min":0}),
            "leads":forms.NumberInput(attrs={"class":"form-control","min":0}),
        }
