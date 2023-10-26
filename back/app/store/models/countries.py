from django.db.models import Model, CharField


class Country(Model):
    title = CharField('Наименование', max_length=50, unique=True)

    class Meta:
        verbose_name = 'Страна марки'
        verbose_name_plural = 'Страны марок'

    def __str__(self):
        return self.title
