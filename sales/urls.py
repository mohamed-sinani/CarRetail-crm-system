fromdjango.urlsimportpath
from.viewsimportSaleCreateView,SaleDeleteView,SaleListView,SaleUpdateView
app_name="sales"
urlpatterns = [
    path("",SaleListView.as_view(),name="list"),
    path("add/",SaleCreateView.as_view(),name="add"),
    path("<int:pk>/edit/",SaleUpdateView.as_view(),name="edit"),
    path("<int:pk>/delete/",SaleDeleteView.as_view(),name="delete"),
]
