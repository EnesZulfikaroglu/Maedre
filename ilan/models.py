from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Ilan(models.Model):
    owner = models.ForeignKey("auth.User", on_delete= models.CASCADE, verbose_name= "İlan Sahibi")
    title = models.CharField(max_length= 50, verbose_name= "Başlık")
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add= True, verbose_name= "Oluşturulma Tarihi")
    ilan_image = models.FileField(blank= True, null= True, verbose_name= "Görsel Ekle:")
    def __str__(self):
        return self.title

class Comment(models.Model):
    ilan = models.ForeignKey(Ilan, on_delete= models.CASCADE, verbose_name= "ilan", related_name= "comments")
    comment_user = models.ForeignKey("auth.user", on_delete= models.CASCADE, verbose_name= "Gönderen")
    comment_content = models.CharField(max_length= 200, verbose_name= "Yorum")
    comment_created_date = models.DateTimeField(auto_now_add= True, verbose_name="Oluşturulma Tarihi")