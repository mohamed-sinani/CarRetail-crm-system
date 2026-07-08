fromdjango.appsimportAppConfig
classAccountsConfig(AppConfig):
    default_auto_field='django.db.models.BigAutoField'
    name='accounts'
    defready(self):
        fromdjango.db.models.signalsimportpost_migrate
        from.signalsimportcreate_default_users
        post_migrate.connect(create_default_users,sender=self)
