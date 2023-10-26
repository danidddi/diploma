from django.db.models import Model, CharField


class Boost(Model):
    title = CharField('Наименование', max_length=50, unique=True)

    class Meta:
        verbose_name = 'Тип наддува'
        verbose_name_plural = 'Типы наддувов'

    def __str__(self):
        return self.title
