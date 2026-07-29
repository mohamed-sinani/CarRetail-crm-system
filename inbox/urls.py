from django.urls import path
from .import views
app_name="inbox"
urlpatterns=[
    path("",views.chat_list,name="list"),
    path("<int:pk>/",views.chat_detail,name="detail"),
    path("api/send/",views.send_message_api,name="send_api"),
    path("api/fetch/",views.fetch_messages_api,name="fetch_api"),
]
