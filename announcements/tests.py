from django.test import TestCase
from .models import Announcement
from accounts.models import User

class AnnouncementModelTest(TestCase):
    def test_create_announcement(self):
        admin=User.objects.create_user(username="admin3",password="pass",role=User.Role.ADMIN,is_superuser=True)
        a=Announcement.objects.create(title="Test Note",message="This is a test.",created_by=admin)
        self.assertEqual(str(a),"Test Note")
