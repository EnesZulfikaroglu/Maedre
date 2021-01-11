from django.contrib import admin
from django.urls import path, include
from ilan import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name= "index"),
    path('about/', views.about, name= "about"),
    path('ilan/', include("ilan.urls")),
    path('user/', include("user.urls")),
    path('message/', include("message.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)