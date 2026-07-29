from django.urls import path
from .import views
urlpatterns = [
    path('',views.home,name='public_home'),
    path('car/<int:pk>/',views.vehicle_detail,name='public_vehicle_detail'),
    path('car/<int:pk>/chat/',views.chat_room,name='public_chat'),
    path('register/',views.register,name='public_register'),
    path('login/',views.customer_login,name='public_login'),
    path('logout/',views.customer_logout,name='public_logout'),
]
