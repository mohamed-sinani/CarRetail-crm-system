fromdjango.contribimportmessages
fromdjango.contrib.auth.mixinsimportLoginRequiredMixin
fromdjango.shortcutsimportredirect
classRoleRequiredMixin(LoginRequiredMixin):
    allowed_roles=()
    defdispatch(self,request,*args,**kwargs):
        ifnotrequest.user.is_authenticated:
            returnsuper().dispatch(request,*args,**kwargs)
        ifrequest.user.is_superuserorrequest.user.roleinself.allowed_roles:
            returnsuper().dispatch(request,*args,**kwargs)
        messages.error(request,"You do not have permission to access that section.")
        returnredirect("dashboard:home")
