  
from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ["username","content", "files"]

class MessageToUserForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ["content", "files"]