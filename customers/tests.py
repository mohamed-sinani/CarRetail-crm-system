from django.test import TestCase
from .models import Customer
from accounts.models import User

class CustomerModelTest(TestCase):
    def test_create_customer(self):
        c=Customer.objects.create(full_name="John Doe",phone="255712345678")
        self.assertEqual(str(c),"John Doe")

    def test_customer_with_salesperson(self):
        sales=User.objects.create_user(username="sales1",password="pass",role=User.Role.SALES)
        c=Customer.objects.create(full_name="Jane Doe",phone="255712345679",assigned_salesperson=sales)
        self.assertEqual(c.assigned_salesperson,sales)
