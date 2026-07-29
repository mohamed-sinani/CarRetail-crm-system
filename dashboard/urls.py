from django.urls import path
from .import views
app_name="dashboard"
urlpatterns = [
    path("",views.dashboard_home,name="home"),
    path("marketing/",views.marketing_home,name="marketing"),
    path("marketing/<int:pk>/edit/",views.campaign_edit,name="campaign_edit"),
    path("marketing/<int:pk>/delete/",views.campaign_delete,name="campaign_delete"),
]
