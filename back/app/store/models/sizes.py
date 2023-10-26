from django.db.models import Model, IntegerField, CharField


class Size(Model):
    length = IntegerField('Длина автомобиля', null=True)
    width = IntegerField('Ширина автомобиля', null=True)
    height = IntegerField('Высота автомобиля', null=True)
    wheelbase = IntegerField('Колёсная база', null=True)
    clearance = CharField('Клиренс', max_length=10, null=True)
    front_track_width = IntegerField('Ширина передней колеи', null=True)
    rear_track_width = IntegerField('Ширина задней колеи', null=True)
    wheel_size = CharField('Размер колёс', max_length=100, null=True)

    class Meta:
        verbose_name = 'Размер автомобиля'
        verbose_name_plural = 'Размеры автомобилей'

    def __str__(self):
        return 'Размер автомобиля'
