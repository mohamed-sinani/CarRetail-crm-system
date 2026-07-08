from django import forms
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from .models import User
class LoginForm(AuthenticationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Username or email"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Password"}))
    def clean(self):
        username=self.cleaned_data.get("username")
        if username and"@"in username:
            try:
                self.cleaned_data["username"]=User.objects.get(email__iexact=username).username
            except User.DoesNotExist:
                pass
        returnsuper().clean()
class UserForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","email","first_name","last_name","role","phone","password1","password2"]
        widgets = {
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "first_name":forms.TextInput(attrs={"class":"form-control"}),
            "last_name":forms.TextInput(attrs={"class":"form-control"}),
            "role":forms.Select(attrs={"class":"form-select"}),
            "phone":forms.TextInput(attrs={"class":"form-control"}),
        }
