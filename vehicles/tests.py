from django.test import TestCase
from .models import Vehicle

class VehicleModelTest(TestCase):
    def test_create_vehicle(self):
        v=Vehicle.objects.create(brand="Honda",model="CB500X",year=2025,price=15000,mileage=0)
        self.assertEqual(str(v),"2025 Honda CB500X")
        self.assertEqual(v.status,Vehicle.Status.AVAILABLE)

    def test_sold_status(self):
        v=Vehicle.objects.create(brand="Yamaha",model="MT-07",year=2024,price=12000,mileage=5000,status=Vehicle.Status.SOLD)
        self.assertEqual(v.get_status_display(),"Sold")
