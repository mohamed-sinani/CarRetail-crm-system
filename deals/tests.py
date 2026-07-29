from django.test import TestCase
from .models import Deal
from accounts.models import User
from customers.models import Customer
from vehicles.models import Vehicle

class DealModelTest(TestCase):
    def setUp(self):
        self.sales=User.objects.create_user(username="sales2",password="pass",role=User.Role.SALES)
        self.customer=Customer.objects.create(full_name="Test Client",phone="255700000001")
        self.vehicle=Vehicle.objects.create(brand="Kawasaki",model="Ninja 400",year=2025,price=8000,mileage=0)

    def test_create_deal(self):
        deal=Deal.objects.create(customer=self.customer,vehicle=self.vehicle,salesperson=self.sales,stage=Deal.Stage.NEW_LEAD)
        self.assertEqual(deal.stage,Deal.Stage.NEW_LEAD)

    def test_deal_str(self):
        deal=Deal.objects.create(customer=self.customer,vehicle=self.vehicle,salesperson=self.sales)
        self.assertIn("Test Client",str(deal))
