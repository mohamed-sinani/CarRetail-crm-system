from django.db import models
from django.conf import settings
class Announcement(models.Model):
    title=models.CharField(max_length=180)
    message=models.TextField()
    created_by=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering=["-created_at"]
    def __str__(self):
        returnself.title
