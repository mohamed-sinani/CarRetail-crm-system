from django.urls import path
from .import views
urlpatterns = [
    path('',views.home,name='public_home'),
    path('motorcycle/<int:pk>/',views.vehicle_detail,name='public_vehicle_detail'),
]
