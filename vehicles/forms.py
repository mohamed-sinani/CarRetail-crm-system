from django import forms
from .models import Vehicle
class VehicleForm(forms.ModelForm):
    class Meta:
        model=Vehicle
        fields=["brand","model","year","price","mileage","transmission","fuel_type","status","image"]
        widgets = {
            "brand":forms.TextInput(attrs={"class":"form-control"}),
            "model":forms.TextInput(attrs={"class":"form-control"}),
            "year":forms.NumberInput(attrs={"class":"form-control"}),
            "price":forms.NumberInput(attrs={"class":"form-control","step":"0.01"}),
            "mileage":forms.NumberInput(attrs={"class":"form-control"}),
            "transmission":forms.Select(attrs={"class":"form-select"}),
            "fuel_type":forms.Select(attrs={"class":"form-select"}),
            "status":forms.Select(attrs={"class":"form-select"}),
            "image":forms.ClearableFileInput(attrs={"class":"form-control"}),
        }
