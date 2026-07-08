from django.urls import path
from .views import DealCreateView,DealDeleteView,DealListView,DealUpdateView
app_name="deals"
urlpatterns = [
    path("",DealListView.as_view(),name="list"),
    path("add/",DealCreateView.as_view(),name="add"),
    path("<int:pk>/edit/",DealUpdateView.as_view(),name="edit"),
    path("<int:pk>/delete/",DealDeleteView.as_view(),name="delete"),
]
