from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
class RoleRequiredMixin(LoginRequiredMixin):
    allowed_roles=()
    def dispatch(self,request,*args,**kwargs):
        if not request.user.is_authenticated:
            return super().dispatch(request,*args,**kwargs)
        if request.user.is_superuser or request.user.role in self.allowed_roles:
            return super().dispatch(request,*args,**kwargs)
        messages.error(request,"You do not have permission to access that section.")
        return redirect("dashboard:home")
