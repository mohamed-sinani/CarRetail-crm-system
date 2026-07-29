from django import forms
from .models import ChatMessage

class ChatMessageForm(forms.ModelForm):
    class Meta:
        model=ChatMessage
        fields=["message"]
        widgets={
            "message":forms.Textarea(attrs={"class":"form-control chat-input","rows":1,"placeholder":"Type a message..."}),
        }
