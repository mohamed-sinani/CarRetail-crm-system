from django.db import models
from django.conf import settings
from django.db.models import Sum
class Customer(models.Model):
    full_name=models.CharField(max_length=140)
    phone=models.CharField(max_length=30)
    email=models.EmailField(blank=True)
    address=models.TextField(blank=True)
    assigned_salesperson = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="assigned_customers",
        limit_choices_to={"role":"SALES"},
    )
    created_at=models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering=["full_name"]
    def __str__(self):
        return self.full_name
    @property
    def total_spent(self):
        return self.sales.aggregate(total=Sum("amount"))["total"] or 0
    @property
    def total_deals_value(self):
        return self.deals.aggregate(total=Sum("expected_value"))["total"] or 0
    @property
    def total_value(self):
        return self.total_spent + self.total_deals_value
