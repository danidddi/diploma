from django.db.models import Model, CharField


class Drive(Model):
    title = CharField('Наименование', max_length=50, unique=True, null=True)

    class Meta:
        verbose_name = 'Тип привода'
        verbose_name_plural = 'Типы приводов'

    def __str__(self):
        return self.title
