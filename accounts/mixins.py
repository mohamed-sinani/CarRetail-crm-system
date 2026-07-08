from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
class RoleRequiredMixin(LoginRequiredMixin):
    allowed_roles=()
    def dispatch(self,request,*args,**kwargs):
        if notrequest.user.is_authenticated:
            returnsuper().dispatch(request,*args,**kwargs)
        if request.user.is_superuserorrequest.user.roleinself.allowed_roles:
            returnsuper().dispatch(request,*args,**kwargs)
        messages.error(request,"You do not have permission to access that section.")
        returnredirect("dashboard:home")
