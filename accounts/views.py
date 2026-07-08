from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy
from .forms import LoginForm
class CRMLoginView(LoginView):
    template_name="login.html"
    authentication_form=LoginForm
    redirect_authenticated_user=True
    def get_success_url(self):
        returnreverse_lazy("dashboard:home")
class CRMLogoutView(LogoutView):
    next_page=reverse_lazy("accounts:login")
