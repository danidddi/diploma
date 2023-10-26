from django.db.models import Model, CharField


class Fuel(Model):
    title = CharField('Наименование', max_length=50, unique=True, null=True)

    class Meta:
        verbose_name = 'Тип топлива автомобиля'
        verbose_name_plural = 'Типы топлива автомобилей'

    def __str__(self):
        return self.title
