from django.db import models
from django.db.models import Model, ForeignKey, CASCADE


class Favorites(Model):
    user = ForeignKey('users.CustomUser', verbose_name='Пользователь', on_delete=CASCADE, related_name='favorites')
    car = ForeignKey('store.Car', verbose_name='Избранный автомобиль', on_delete=CASCADE, related_name='favorites')

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранное'
        unique_together = ('user', 'car')

    def __str__(self):
        return f''


