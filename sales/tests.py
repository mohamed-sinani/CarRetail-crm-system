from django.test import TestCase
from .models import Sale
from accounts.models import User
from customers.models import Customer
from vehicles.models import Vehicle
from django.utils import timezone

class SaleModelTest(TestCase):
    def setUp(self):
        self.sales=User.objects.create_user(username="sales3",password="pass",role=User.Role.SALES)
        self.customer=Customer.objects.create(full_name="Buyer One",phone="255700000002")
        self.vehicle=Vehicle.objects.create(brand="Suzuki",model="V-Strom 650",year=2024,price=11000,mileage=2000)

    def test_create_sale_marks_vehicle_sold(self):
        from django.utils import timezone
        sale=Sale.objects.create(vehicle=self.vehicle,customer=self.customer,salesperson=self.sales,amount=11000,sale_date=timezone.localdate(),payment_method=Sale.PaymentMethod.CASH)
        self.vehicle.refresh_from_db()
        self.assertEqual(self.vehicle.status,Vehicle.Status.SOLD)
