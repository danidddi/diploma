from django.db.models import Model, CharField


class Color(Model):
    title = CharField('Наименование', max_length=50, unique=True)

    class Meta:
        verbose_name = 'Цвет автомобиля'
        verbose_name_plural = 'Цвета автомобилей'

    def __str__(self):
        return self.title
