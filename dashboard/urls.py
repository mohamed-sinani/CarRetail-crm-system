fromdjango.urlsimportpath
from.importviews
app_name="dashboard"
urlpatterns = [
    path("",views.dashboard_home,name="home"),
    path("marketing/",views.marketing_home,name="marketing"),
]
