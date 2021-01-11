from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "message"

urlpatterns = [
    path('', views.msgIndex, name="msgIndex"),
    path('sendMessage', views.sendMessage, name="sendMessage"),
    path('inbox', views.inbox, name="inbox"),
    path('outbox', views.outbox, name="outbox"),
    path('details/<int:id>', views.details, name="details"),
    path('sendMessageToUser/<int:id>', views.sendMessageToUser, name="sendMessageToUser"),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)