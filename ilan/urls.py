from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "ilan"

urlpatterns = [
    path('dashboard/', views.dashboard, name= "dashboard"),
    path('addIlan/', views.addIlan, name= "addIlan"),
    path('showIlans/', views.showIlans, name= "showIlans"),
    path('showAll/', views.showAll, name= "showAll"),
    path('details/<int:id>', views.detail, name= "details"),
    path('update/<int:id>', views.updateIlan, name= "update"),
    path('delete/<int:id>', views.deleteIlan, name= "delete"),
    path('addComment/<int:id>', views.addComment, name= "addComment"),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)