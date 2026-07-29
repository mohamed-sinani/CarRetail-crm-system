from django.contrib.auth.models import AbstractUser
from django.db import models
class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN="ADMIN","Admin"
        MARKETING="MARKETING","Marketing"
        SALES="SALES","Sales"
        CUSTOMER="CUSTOMER","Customer"
    role=models.CharField(max_length=20,choices=Role.choices,default=Role.CUSTOMER)
    phone=models.CharField(max_length=30,blank=True)
    @property
    def is_admin_role(self):
        return self.role==self.Role.ADMIN or self.is_superuser
    @property
    def is_marketing_role(self):
        return self.role==self.Role.MARKETING
    @property
    def is_sales_role(self):
        return self.role==self.Role.SALES
