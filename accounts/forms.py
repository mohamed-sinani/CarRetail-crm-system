from django import forms
from django.contrib.auth.forms import AuthenticationForm
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
        return super().clean()
