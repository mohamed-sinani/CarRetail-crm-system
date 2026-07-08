fromdjangoimportforms
from.modelsimportDeal
classDealForm(forms.ModelForm):
    classMeta:
        model=Deal
        fields=["customer","vehicle","salesperson","stage","expected_value","notes"]
        widgets = {
            "customer":forms.Select(attrs={"class":"form-select"}),
            "vehicle":forms.Select(attrs={"class":"form-select"}),
            "salesperson":forms.Select(attrs={"class":"form-select"}),
            "stage":forms.Select(attrs={"class":"form-select"}),
            "expected_value":forms.NumberInput(attrs={"class":"form-control","step":"0.01"}),
            "notes":forms.Textarea(attrs={"class":"form-control","rows":3}),
        }
