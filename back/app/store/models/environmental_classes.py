from django.db.models import Model, CharField


class EnvironmentalClass(Model):
    title = CharField('Наименование', max_length=50, unique=True)

    class Meta:
        verbose_name = 'Экологический класс'
        verbose_name_plural = 'Экологические классы'

    def __str__(self):
        return self.title
