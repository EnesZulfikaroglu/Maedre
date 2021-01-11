from django.db import models

# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey("auth.User", on_delete= models.CASCADE, related_name= "profile")
    name = models.CharField(max_length=50, verbose_name="Ad", blank=True, null=True)
    surname = models.CharField(max_length=50, verbose_name="Soyad", blank=True, null=True)
    email = models.EmailField(max_length=50, verbose_name="E-mail", blank=True, null=True)
    about = models.CharField(max_length=150, verbose_name="Hakkında", blank=True, null=True)
    photo = models.FileField(upload_to='Photo/', blank=True, null=True, verbose_name= "Profil Fotoğrafı Ekle")


    instagram = models.CharField(max_length=30, verbose_name="İnstagram", blank=True, null=True, help_text= "Instagram linkinizi koyunuz.")
    twitter = models.CharField(max_length=30, verbose_name="Twitter", blank=True, null=True, help_text="Twitter linkinizi koyunuz.")
    facebook = models.CharField(max_length=30, verbose_name="Facebook", blank=True, null=True, help_text="Facebook linkinizi koyunuz.")

    high_school = models.CharField(max_length=50, verbose_name="Lise", blank=True, null=True, help_text="Profil linkinizi koyunuz.")
    university = models.CharField(max_length=50, verbose_name="Üniversite", blank=True, null=True, help_text="Profil linkinizi koyunuz.")