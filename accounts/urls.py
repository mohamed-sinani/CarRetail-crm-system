from django.urls import path
from .views import CRMLoginView,CRMLogoutView
app_name="accounts"
urlpatterns = [
    path("login/",CRMLoginView.as_view(),name="login"),
    path("logout/",CRMLogoutView.as_view(),name="logout"),
]
