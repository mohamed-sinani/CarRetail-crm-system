from django.test import TestCase
from .models import User

class UserModelTest(TestCase):
    def test_create_user(self):
        user=User.objects.create_user(username="testuser",password="testpass123",role=User.Role.SALES)
        self.assertEqual(user.role,User.Role.SALES)
        self.assertTrue(user.is_sales_role)

    def test_admin_role(self):
        user=User.objects.create_user(username="admin2",password="pass",role=User.Role.ADMIN,is_superuser=True)
        self.assertTrue(user.is_admin_role)
