from django.db import models
class ReportSnapshot(models.Model):
    class ReportType(models.TextChoices):
        SALES="SALES","Sales"
        INVENTORY="INVENTORY","Inventory"
        REVENUE="REVENUE","Revenue"
    report_type=models.CharField(max_length=20,choices=ReportType.choices)
    title=models.CharField(max_length=160)
    generated_at=models.DateTimeField(auto_now_add=True)
    payload=models.JSONField(default=dict,blank=True)
    class Meta:
        ordering=["-generated_at"]
    def __str__(self):
        return self.title
