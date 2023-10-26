from django.db.models import Model, CharField, ForeignKey, CASCADE, BooleanField, IntegerField, TextField


class Car(Model):
    model = CharField('Модель', max_length=50)
    is_stock = BooleanField('Статус наличия')
    is_customs = BooleanField('Статус растаможивания')
    is_deleted = BooleanField('Статус удаления')
    year = IntegerField('Год выпуска автомобиля')
    cost = IntegerField('Стоимость')
    description = TextField('Описание', default='')
    youtube_url = CharField('Ссылка на видеообзор', max_length=100, default='')

    brand = ForeignKey('store.Brand', verbose_name='Брэнд автомобиля', on_delete=CASCADE, related_name='car')
    car_body = ForeignKey('store.CarBody', verbose_name='Тип кузова автомобиля', on_delete=CASCADE, related_name='car')
    exterior_color = ForeignKey('store.Color', verbose_name='Цвет экстерьера автомобиля', on_delete=CASCADE,
                                related_name='car')
    characteristics = ForeignKey('store.Characteristics', verbose_name='Детальные характеристики', on_delete=CASCADE,
                                 related_name='car', null=True)


    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'

    def __str__(self):
        return f'{self.exterior_color} {self.brand} {self.model} {self.car_body} {self.year}'

