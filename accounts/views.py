from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .forms import LoginForm
class CRMLoginView(LoginView):
    template_name="login.html"
    authentication_form=LoginForm
    redirect_authenticated_user=True
    def get_success_url(self):
        return reverse_lazy("dashboard:home")
def crm_logout(request):
    if request.method=="POST":
        logout(request)
    return redirect("accounts:login")
