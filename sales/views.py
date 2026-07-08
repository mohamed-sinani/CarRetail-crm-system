from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView,DeleteView,ListView,UpdateView
from accounts.mixins import RoleRequiredMixin
from .forms import SaleForm
from .models import Sale
class SaleListView(RoleRequiredMixin,ListView):
    allowed_roles=("ADMIN","SALES")
    model=Sale
    template_name="sales.html"
    context_object_name="sales"
    def get_queryset(self):
        return Sale.objects.select_related("vehicle","customer","salesperson")
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context["page_title"]="Sales"
        context["form"]=SaleForm(initial={"salesperson":self.request.user if self.request.user.role=="SALES" else None})
        returncontext
class SaleCreateView(RoleRequiredMixin,CreateView):
    allowed_roles=("ADMIN","SALES")
    model=Sale
    form_class=SaleForm
    success_url=reverse_lazy("sales:list")
    def form_valid(self,form):
        messages.success(self.request,"Sale recorded and vehicle marked as sold.")
        return super().form_valid(form)
class SaleUpdateView(RoleRequiredMixin,UpdateView):
    allowed_roles=("ADMIN","SALES")
    model=Sale
    form_class=SaleForm
    template_name="form.html"
    success_url=reverse_lazy("sales:list")
class SaleDeleteView(RoleRequiredMixin,DeleteView):
    allowed_roles=("ADMIN",)
    model=Sale
    template_name="confirm_delete.html"
    success_url=reverse_lazy("sales:list")
