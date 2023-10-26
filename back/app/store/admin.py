from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.utils.safestring import mark_safe

from store.models import Car, Brand, CarBody, Color, Fuel, Image, Boost, Drive, Characteristics, Gear, Size, Country
from store.models import EnvironmentalClass, Bid

admin.site.site_title = 'Администрирование автосалона'
admin.site.site_header = 'Администрирование автосалона'

class ImageInlines(admin.StackedInline):
    model = Image
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="300">')

    get_image.short_description = "Изображение"

    extra = 1


# Register your models here.
@admin.register(Car)
class CarAdmin(ModelAdmin):
    list_filter = ("brand__title",)
    inlines = [ImageInlines]
    save_on_top = True
#
#
#
# @admin.register(Brand)
# class BrandAdmin(ModelAdmin):
#     pass
#
#
# @admin.register(CarBody)
# class CarBodyAdmin(ModelAdmin):
#     pass
#
#
# @admin.register(Color)
# class ColorAdmin(ModelAdmin):
#     pass
#
#
# @admin.register(Fuel)
# class FuelAdmin(ModelAdmin):
#     pass
#
#
# @admin.register(Image)
# class ImageAdmin(ModelAdmin):
#     readonly_fields = ("get_image",)
#
#     def get_image(self, obj):
#         return mark_safe(f'<img src={obj.image.url} width="300">')
#
#     get_image.short_description = "Изображение"
#
#
# @admin.register(Boost)
# class BoostAdmin(ModelAdmin):
#     pass


@admin.register(Bid)
class BidAdmin(ModelAdmin):
    list_display = ("id", "name", "phone", "email", "date_open_bid", "date_close_bid")
    list_display_links = ("id", "name", "phone", "email",)
    list_filter = ("date_close_bid",)
    search_fields = ("name", "phone", "email")
    readonly_fields = ("name", "phone", "email", "date_open_bid")

#
# @admin.register(Drive)
# class DriveAdmin(ModelAdmin):
#     pass
#
#
# @admin.register(Characteristics)
# class CharacteristicsAdmin(ModelAdmin):
#     pass
#
#
# @admin.register(Gear)
# class GearAdmin(ModelAdmin):
#     pass
#
#
# @admin.register(Size)
# class SizeAdmin(ModelAdmin):
#     pass
#
#
# @admin.register(Country)
# class CountryAdmin(ModelAdmin):
#     pass
#
#
# @admin.register(EnvironmentalClass)
# class EnvironmentalClassAdmin(ModelAdmin):
#     pass
