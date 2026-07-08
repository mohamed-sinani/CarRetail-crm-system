from django.urls import path
from .views import CustomerCreateView,CustomerDeleteView,CustomerListView,CustomerUpdateView
app_name="customers"
urlpatterns = [
    path("",CustomerListView.as_view(),name="list"),
    path("add/",CustomerCreateView.as_view(),name="add"),
    path("<int:pk>/edit/",CustomerUpdateView.as_view(),name="edit"),
    path("<int:pk>/delete/",CustomerDeleteView.as_view(),name="delete"),
]
