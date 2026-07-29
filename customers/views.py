from django.contrib import messages
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import CreateView,DeleteView,ListView,UpdateView
from accounts.mixins import RoleRequiredMixin
from .forms import CustomerForm
from .models import Customer
class CustomerListView(RoleRequiredMixin,ListView):
    allowed_roles=("ADMIN","SALES")
    model=Customer
    template_name="contacts.html"
    context_object_name="customers"
    def get_queryset(self):
        queryset=Customer.objects.select_related("assigned_salesperson").all()
        query=self.request.GET.get("q","")
        if query:
            queryset=queryset.filter(Q(full_name__icontains=query)|Q(phone__icontains=query)|Q(email__icontains=query))
        return queryset
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context["page_title"]="Contacts"
        context["form"]=CustomerForm()
        return context
class CustomerCreateView(RoleRequiredMixin,CreateView):
    allowed_roles=("ADMIN","SALES")
    model=Customer
    form_class=CustomerForm
    success_url=reverse_lazy("customers:list")
    def form_valid(self,form):
        messages.success(self.request,"Customer profile saved.")
        return super().form_valid(form)
class CustomerUpdateView(RoleRequiredMixin,UpdateView):
    allowed_roles=("ADMIN","SALES")
    model=Customer
    form_class=CustomerForm
    template_name="form.html"
    success_url=reverse_lazy("customers:list")
class CustomerDeleteView(RoleRequiredMixin,DeleteView):
    allowed_roles=("ADMIN",)
    model=Customer
    template_name="confirm_delete.html"
    success_url=reverse_lazy("customers:list")
