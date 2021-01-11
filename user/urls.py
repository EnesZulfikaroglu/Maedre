from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "user"

urlpatterns = [
    path('register/', views.register, name= "register"),
    path('login/', views.loginUser, name= "login"),
    path('logout/', views.logoutUser, name= "logout"),
    path('profile/<int:id>', views.showProfile, name= "profile"),
    path('updateProfile/<int:id>', views.updateProfile, name= "updateProfile"),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)