from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Message(models.Model):
    sender = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name="Gönderen")
    reciever = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name="Alıcı")
    username = models.CharField(max_length=20, default="", verbose_name="Kullanıcı Adı:")
    content = RichTextField(verbose_name= "Mesaj:")
    files = models.FileField(upload_to='Messages/', null=True, blank=True, verbose_name= "Dosya Ekle:")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Gönderim Tarihi")