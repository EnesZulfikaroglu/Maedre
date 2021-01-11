from django.contrib import admin

from .models import Ilan, Comment

# Register your models here.

@admin.register(Ilan)
class IlanAdmin(admin.ModelAdmin):

    list_display = ["title","owner","created_date"]

    search_fields = ["title"]

    list_filter = ["created_date"]

    class Meta:
        model = Ilan

admin.site.register(Comment)