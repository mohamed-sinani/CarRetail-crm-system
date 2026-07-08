fromdjango.core.management.baseimportBaseCommand
fromaccounts.signalsimportcreate_default_users
classCommand(BaseCommand):
    help="Create the default CRM users."
    defhandle(self,*args,**options):
        create_default_users()
        self.stdout.write(self.style.SUCCESS("Default CRM users are ready."))
