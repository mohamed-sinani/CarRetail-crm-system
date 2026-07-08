from django.core.management.base import BaseCommand
from accounts.signals import create_default_users
class Command(BaseCommand):
    help="Create the default CRM users."
    def handle(self,*args,**options):
        create_default_users()
        self.stdout.write(self.style.SUCCESS("Default CRM users are ready."))
