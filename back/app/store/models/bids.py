from django.db.models import Model, CharField, DateField, ForeignKey, CASCADE


class Bid(Model):
    name = CharField('ФИО клиента', null=True)
    email = CharField('Почта клиента', max_length=50)
    phone = CharField('Телефон клиента', max_length=13)
    car = ForeignKey('store.Car', verbose_name='Интерисующий автомобиль', on_delete=CASCADE, related_name='bid',
                     null=True, blank=True)
    date_open_bid = DateField('Дата открытия заявки', null=True, blank=True)
    date_close_bid = DateField('Дата закрытия заявки', null=True, blank=True)

    class Meta:
        verbose_name = 'Заявка на консультацию'
        verbose_name_plural = 'Заявки на консультацию'

    def __str__(self):
        return self.name
