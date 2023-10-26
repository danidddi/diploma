from django.db.models import Model, CharField


class Gear(Model):
    title = CharField('Наименование', max_length=50, unique=True, null=True)

    class Meta:
        verbose_name = 'Тип коробки автомобиля'
        verbose_name_plural = 'Типы коробки автомобилей'

    def __str__(self):
        return self.title
