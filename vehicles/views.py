from django.contrib import messages
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import CreateView,DeleteView,ListView,UpdateView
from accounts.mixins import RoleRequiredMixin
from .forms import VehicleForm
from .models import Vehicle
class VehicleListView(RoleRequiredMixin,ListView):
    allowed_roles=("ADMIN",)
    model=Vehicle
    template_name="vehicles.html"
    context_object_name="vehicles"
    paginate_by=12
    def get_queryset(self):
        queryset=Vehicle.objects.all()
        query=self.request.GET.get("q","")
        status=self.request.GET.get("status","")
        if query:
            queryset=queryset.filter(Q(brand__icontains=query)|Q(model__icontains=query))
        if status:
            queryset=queryset.filter(status=status)
        return queryset
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context["page_title"]="Vehicles"
        context["form"]=VehicleForm()
        context["statuses"]=Vehicle.Status.choices
        return context
class VehicleCreateView(RoleRequiredMixin,CreateView):
    allowed_roles=("ADMIN",)
    model=Vehicle
    form_class=VehicleForm
    success_url=reverse_lazy("vehicles:list")
    def form_valid(self,form):
        messages.success(self.request,"Vehicle added to inventory.")
        return super().form_valid(form)
class VehicleUpdateView(RoleRequiredMixin,UpdateView):
    allowed_roles=("ADMIN",)
    model=Vehicle
    form_class=VehicleForm
    template_name="form.html"
    success_url=reverse_lazy("vehicles:list")
    def form_valid(self,form):
        messages.success(self.request,"Vehicle updated.")
        return super().form_valid(form)
class VehicleDeleteView(RoleRequiredMixin,DeleteView):
    allowed_roles=("ADMIN",)
    model=Vehicle
    template_name="confirm_delete.html"
    success_url=reverse_lazy("vehicles:list")
