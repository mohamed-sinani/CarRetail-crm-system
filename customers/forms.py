fromdjangoimportforms
fromdjango.contrib.authimportget_user_model
fromdjango.utils.textimportslugify
from.modelsimportCustomer
classCustomerForm(forms.ModelForm):
    new_salesperson = forms.CharField(
        required=False,
        label="New salesperson",
        help_text="Type a salesperson name to add them to the Sales dropdown.",
        widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Example: Asha Mwinyi"}),
    )
    classMeta:
        model=Customer
        fields=["full_name","phone","email","address","assigned_salesperson"]
        widgets = {
            "full_name":forms.TextInput(attrs={"class":"form-control"}),
            "phone":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "address":forms.Textarea(attrs={"class":"form-control","rows":3}),
            "assigned_salesperson":forms.Select(attrs={"class":"form-select"}),
        }
    def__init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        User=get_user_model()
        self.fields["assigned_salesperson"].queryset = User.objects.filter(role=User.Role.SALES).order_by(
            "first_name",
            "last_name",
            "username",
        )
        self.fields["assigned_salesperson"].required=False
    defsave(self,commit=True):
        customer=super().save(commit=False)
        salesperson_name=self.cleaned_data.get("new_salesperson","").strip()
        ifsalesperson_name:
            customer.assigned_salesperson=self._get_or_create_salesperson(salesperson_name)
        ifcommit:
            customer.save()
            self.save_m2m()
        returncustomer
    def_get_or_create_salesperson(self,name):
        User=get_user_model()
        parts=name.split()
        first_name=parts[0]
        last_name=" ".join(parts[1:])
        base_username=slugify(name).replace("-",".")or"salesperson"
        existing_user=User.objects.filter(role=User.Role.SALES,username__iexact=base_username).first()
        ifnotexisting_userandlast_name:
            existing_user = User.objects.filter(
                role=User.Role.SALES,
                first_name__iexact=first_name,
                last_name__iexact=last_name,
            ).first()
        ifnotexisting_user:
            existing_user=User.objects.filter(role=User.Role.SALES,first_name__iexact=name).first()
        ifexisting_user:
            returnexisting_user
        username=base_username
        counter=1
        whileUser.objects.filter(username=username).exists():
            counter+=1
            username=f"{base_username}{counter}"
        user=User(username=username,first_name=first_name,last_name=last_name,role=User.Role.SALES)
        user.set_unusable_password()
        user.save()
        returnuser
