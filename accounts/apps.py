from django.apps import AppConfig
class AccountsConfig(AppConfig):
    default_auto_field='django.db.models.BigAutoField'
    name='accounts'
    def ready(self):
        from django.db.models.signals import post_migrate
        from .signals import create_default_users
        post_migrate.connect(create_default_users,sender=self)
