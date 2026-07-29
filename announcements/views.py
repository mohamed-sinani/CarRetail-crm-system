from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView,DeleteView,ListView,UpdateView
from accounts.mixins import RoleRequiredMixin
from .forms import AnnouncementForm
from .models import Announcement
class AnnouncementListView(RoleRequiredMixin,ListView):
    allowed_roles=("ADMIN","MARKETING")
    model=Announcement
    template_name="announcements.html"
    context_object_name="announcements"
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context["page_title"]="Announcement"
        context["form"]=AnnouncementForm()
        return context
class AnnouncementCreateView(RoleRequiredMixin,CreateView):
    allowed_roles=("ADMIN","MARKETING")
    model=Announcement
    form_class=AnnouncementForm
    template_name="announcements.html"
    success_url=reverse_lazy("announcements:list")
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context["page_title"]="Announcement"
        context["announcements"]=Announcement.objects.all()
        return context
    def form_valid(self,form):
        form.instance.created_by=self.request.user
        messages.success(self.request,"Announcement published.")
        return super().form_valid(form)
class AnnouncementUpdateView(RoleRequiredMixin,UpdateView):
    allowed_roles=("ADMIN","MARKETING")
    model=Announcement
    form_class=AnnouncementForm
    template_name="form.html"
    success_url=reverse_lazy("announcements:list")
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context["page_title"]="Edit Announcement"
        return context
    def form_valid(self,form):
        messages.success(self.request,"Announcement updated.")
        return super().form_valid(form)
class AnnouncementDeleteView(RoleRequiredMixin,DeleteView):
    allowed_roles=("ADMIN","MARKETING")
    model=Announcement
    template_name="confirm_delete.html"
    success_url=reverse_lazy("announcements:list")
    def delete(self,request,*args,**kwargs):
        messages.success(self.request,"Announcement deleted.")
        return super().delete(request,*args,**kwargs)
