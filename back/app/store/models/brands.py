from django.db.models import Model, CharField


class Brand(Model):
    title = CharField('Наименование', max_length=50, unique=True)

    class Meta:
        verbose_name = 'Брэнд автомобиля'
        verbose_name_plural = 'Брэнды автомобилей'

    def __str__(self):
        return self.title