from django.contrib.admin import ModelAdmin
from django.contrib import admin
from favorites.models import Favorites

@admin.register(Favorites)
class FavoritesAdmin(ModelAdmin):
    list_display = ("user", "car",)
    list_display_links = ("user", "car",)
