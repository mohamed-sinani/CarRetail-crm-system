from django.urls import path
from .views import VehicleCreateView,VehicleDeleteView,VehicleListView,VehicleUpdateView
app_name="vehicles"
urlpatterns = [
    path("",VehicleListView.as_view(),name="list"),
    path("add/",VehicleCreateView.as_view(),name="add"),
    path("<int:pk>/edit/",VehicleUpdateView.as_view(),name="edit"),
    path("<int:pk>/delete/",VehicleDeleteView.as_view(),name="delete"),
]
