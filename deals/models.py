from django.db import models
from django.conf import settings
class Deal(models.Model):
    class Stage(models.TextChoices):
        NEW_LEAD="NEW_LEAD","New Lead"
        CONTACTED="CONTACTED","Contacted"
        NEGOTIATION="NEGOTIATION","Negotiation"
        PAYMENT_PENDING="PAYMENT_PENDING","Payment Pending"
        CLOSED_WON="CLOSED_WON","Closed Won"
        CLOSED_LOST="CLOSED_LOST","Closed Lost"
    customer=models.ForeignKey("customers.Customer",on_delete=models.CASCADE,related_name="deals")
    vehicle=models.ForeignKey("vehicles.Vehicle",on_delete=models.CASCADE,related_name="deals")
    salesperson=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,null=True,related_name="deals")
    stage=models.CharField(max_length=30,choices=Stage.choices,default=Stage.NEW_LEAD)
    expected_value=models.DecimalField(max_digits=12,decimal_places=2,default=0)
    notes=models.TextField(blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    class Meta:
        ordering=["stage","-updated_at"]
    def __str__(self):
        return f"{self.customer} - {self.vehicle}"
