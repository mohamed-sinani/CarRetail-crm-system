from django import forms
from .models import MarketingCampaign
class MarketingCampaignForm(forms.ModelForm):
    class Meta:
        model=MarketingCampaign
        fields=["title","channel","message","link_url","views","replies","leads"]
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
            "link_url":forms.TextInput(attrs={"class":"form-control","placeholder":"WhatsApp number or Instagram/Facebook URL"}),
            "views":forms.NumberInput(attrs={"class":"form-control","min":0}),
            "replies":forms.NumberInput(attrs={"class":"form-control","min":0}),
            "leads":forms.NumberInput(attrs={"class":"form-control","min":0}),
        }
