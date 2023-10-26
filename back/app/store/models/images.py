from django.db.models import Model, CharField, ImageField, ForeignKey, CASCADE

from store.models import Car


class Image(Model):
    image = ImageField(upload_to='images/', blank=True)
    car = ForeignKey('store.Car', verbose_name='Автомобиль', null=True, on_delete=CASCADE, related_name='images')


    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

