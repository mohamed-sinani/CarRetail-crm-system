from django.urls import path
from .views import AnnouncementCreateView,AnnouncementDeleteView,AnnouncementListView,AnnouncementUpdateView
app_name="announcements"
urlpatterns = [
    path("",AnnouncementListView.as_view(),name="list"),
    path("add/",AnnouncementCreateView.as_view(),name="add"),
    path("<int:pk>/edit/",AnnouncementUpdateView.as_view(),name="edit"),
    path("<int:pk>/delete/",AnnouncementDeleteView.as_view(),name="delete"),
]
