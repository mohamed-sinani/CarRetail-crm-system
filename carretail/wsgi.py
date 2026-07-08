
importos
fromdjango.core.wsgiimportget_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE','carretail.settings')
application=get_wsgi_application()
