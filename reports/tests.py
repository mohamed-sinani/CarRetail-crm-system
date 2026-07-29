from django.test import TestCase
from .models import ReportSnapshot

class ReportSnapshotModelTest(TestCase):
    def test_create_snapshot(self):
        r=ReportSnapshot.objects.create(report_type=ReportSnapshot.ReportType.SALES,title="Monthly Sales",payload={"count":5})
        self.assertEqual(str(r),"Monthly Sales")
