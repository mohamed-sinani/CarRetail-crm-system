from django.conf import settings
from django.db import models

class ChatSession(models.Model):
    class Status(models.TextChoices):
        ACTIVE="ACTIVE","Active"
        CLOSED="CLOSED","Closed"
    vehicle=models.ForeignKey("vehicles.Vehicle",on_delete=models.CASCADE,related_name="chat_sessions")
    customer=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="chat_sessions")
    assigned_to=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,null=True,blank=True,related_name="assigned_chats")
    status=models.CharField(max_length=20,choices=Status.choices,default=Status.ACTIVE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    class Meta:
        ordering=["-updated_at"]
        unique_together=["vehicle","customer"]
    def __str__(self):
        return f"{self.customer.username} - {self.vehicle}"

class ChatMessage(models.Model):
    session=models.ForeignKey(ChatSession,on_delete=models.CASCADE,related_name="messages")
    sender=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    message=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    is_read=models.BooleanField(default=False)
    class Meta:
        ordering=["created_at"]
    def __str__(self):
        return f"{self.sender.username}: {self.message[:50]}"
