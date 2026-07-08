from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView,DeleteView,ListView,UpdateView
from accounts.mixins import RoleRequiredMixin
from .forms import DealForm
from .models import Deal
class DealListView(RoleRequiredMixin,ListView):
    allowed_roles=("ADMIN","SALES")
    model=Deal
    template_name="deals.html"
    context_object_name="deals"
    def get_queryset(self):
        return Deal.objects.select_related("customer","vehicle","salesperson")
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        deals_by_stage={}
        for key, label in Deal.Stage.choices:
            deals_by_stage[key] = {
                "label":label,
                "deals":[deal for deal in context["deals"] if deal.stage==key],
            }
        context["page_title"]="Deals"
        context["form"]=DealForm(initial={"salesperson":self.request.user if self.request.user.role=="SALES" else None})
        context["deals_by_stage"]=deals_by_stage
        returncontext
class DealCreateView(RoleRequiredMixin,CreateView):
    allowed_roles=("ADMIN","SALES")
    model=Deal
    form_class=DealForm
    success_url=reverse_lazy("deals:list")
    def form_valid(self,form):
        messages.success(self.request,"Deal added to the pipeline.")
        return super().form_valid(form)
class DealUpdateView(RoleRequiredMixin,UpdateView):
    allowed_roles=("ADMIN","SALES")
    model=Deal
    form_class=DealForm
    template_name="form.html"
    success_url=reverse_lazy("deals:list")
class DealDeleteView(RoleRequiredMixin,DeleteView):
    allowed_roles=("ADMIN",)
    model=Deal
    template_name="confirm_delete.html"
    success_url=reverse_lazy("deals:list")
