from django.db.models import Model, CharField


class CarBody(Model):
    title = CharField('Наименование', max_length=20, unique=True)

    class Meta:
        verbose_name = 'Тип кузова автомобиля'
        verbose_name_plural = 'Типы кузовов автомобилей'

    def __str__(self):
        return self.title
