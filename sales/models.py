from django.db import models
from django.conf import settings
class Sale(models.Model):
    class PaymentMethod(models.TextChoices):
        CASH="CASH","Cash"
        BANK_TRANSFER="BANK_TRANSFER","Bank Transfer"
        FINANCE="FINANCE","Finance"
        CARD="CARD","Card"
    vehicle=models.OneToOneField("vehicles.Vehicle",on_delete=models.PROTECT,related_name="sale")
    customer=models.ForeignKey("customers.Customer",on_delete=models.PROTECT,related_name="sales")
    salesperson=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,null=True,related_name="sales")
    amount=models.DecimalField(max_digits=12,decimal_places=2)
    payment_method=models.CharField(max_length=30,choices=PaymentMethod.choices)
    sale_date=models.DateField()
    created_at=models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering=["-sale_date","-created_at"]
    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        if self.vehicle.status!="SOLD":
            self.vehicle.status="SOLD"
            self.vehicle.save(update_fields=["status","updated_at"])
    def __str__(self):
        return f"{self.vehicle} sold to {self.customer}"
