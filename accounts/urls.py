from django.urls import path
from .views import CRMLoginView,crm_logout
app_name="accounts"
urlpatterns = [
    path("login/",CRMLoginView.as_view(),name="login"),
    path("logout/",crm_logout,name="logout"),
]
