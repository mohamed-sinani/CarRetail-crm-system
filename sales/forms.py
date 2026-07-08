fromdjangoimportforms
fromdjango.contrib.authimportget_user_model
from.modelsimportSale
classSaleForm(forms.ModelForm):
    classMeta:
        model=Sale
        fields=["vehicle","customer","salesperson","amount","payment_method","sale_date"]
        widgets = {
            "vehicle":forms.Select(attrs={"class":"form-select"}),
            "customer":forms.Select(attrs={"class":"form-select"}),
            "salesperson":forms.Select(attrs={"class":"form-select"}),
            "amount":forms.NumberInput(attrs={"class":"form-control","step":"0.01"}),
            "payment_method":forms.Select(attrs={"class":"form-select"}),
            "sale_date":forms.DateInput(attrs={"class":"form-control","type":"date"}),
        }
    def__init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        User=get_user_model()
        self.fields["salesperson"].queryset = User.objects.filter(role=User.Role.SALES).order_by(
            "first_name",
            "last_name",
            "username",
        )
