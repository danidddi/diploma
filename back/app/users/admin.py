from django.contrib.admin import ModelAdmin
from django.contrib import admin
from users.models import CustomUser

@admin.register(CustomUser)
class FuelAdmin(ModelAdmin):
    list_display = ("id", "username", "phone", "email",)
    list_display_links = ("id", "username", "phone", "email",)
    search_fields = ("username", "phone", "email")
    list_filter = ("is_staff",)
