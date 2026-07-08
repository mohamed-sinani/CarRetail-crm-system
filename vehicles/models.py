from django.db import models
class Vehicle(models.Model):
    class Status(models.TextChoices):
        AVAILABLE="AVAILABLE","Available"
        RESERVED="RESERVED","Reserved"
        SOLD="SOLD","Sold"
    class Transmission(models.TextChoices):
        AUTOMATIC="AUTOMATIC","Automatic"
        MANUAL="MANUAL","Manual"
        CVT="CVT","CVT"
    class FuelType(models.TextChoices):
        PETROL="PETROL","Petrol"
        DIESEL="DIESEL","Diesel"
        HYBRID="HYBRID","Hybrid"
        ELECTRIC="ELECTRIC","Electric"
    brand=models.CharField(max_length=80)
    model=models.CharField(max_length=80)
    year=models.PositiveIntegerField()
    price=models.DecimalField(max_digits=12,decimal_places=2)
    mileage=models.PositiveIntegerField()
    transmission=models.CharField(max_length=20,choices=Transmission.choices)
    fuel_type=models.CharField(max_length=20,choices=FuelType.choices)
    status=models.CharField(max_length=20,choices=Status.choices,default=Status.AVAILABLE)
    image=models.FileField(upload_to="vehicles/",blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    class Meta:
        ordering=["brand","model","-year"]
    def __str__(self):
        return f"{self.year} {self.brand} {self.model}"
