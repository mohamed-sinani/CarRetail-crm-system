
fromdjango.contribimportadmin
fromdjango.confimportsettings
fromdjango.conf.urls.staticimportstatic
fromdjango.urlsimportinclude,path
urlpatterns = [
    path('admin/',admin.site.urls),
    path('',include('public.urls')),
    path('dashboard/',include('dashboard.urls')),
    path('accounts/',include('accounts.urls')),
    path('vehicles/',include('vehicles.urls')),
    path('customers/',include('customers.urls')),
    path('deals/',include('deals.urls')),
    path('sales/',include('sales.urls')),
    path('announcements/',include('announcements.urls')),
    path('reports/',include('reports.urls')),
]
ifsettings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
