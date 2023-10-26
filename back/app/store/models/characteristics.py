from django.db.models import Model, CharField, IntegerField, ForeignKey, CASCADE, DecimalField


class Characteristics(Model):
    horse_powers = IntegerField('Лошадиные силы', null=True)
    engine_capacity = DecimalField('Объем двигателя', max_digits=2, decimal_places=1, null=True)
    number_of_doors = IntegerField('Количество дверей', null=True)
    number_of_seats = IntegerField('Количество мест', null=True)
    wheel_position = CharField('Расположение руля', max_length=20, null=True)
    front_suspension = CharField('Тип передней подвески', max_length=50, null=True)
    rear_suspension = CharField('Тип задней подвески', max_length=50, null=True)
    front_brakes = CharField('Передние тормоза', max_length=50, null=True)
    rear_brakes = CharField('Задние  тормоза', max_length=50, null=True)
    max_speed = IntegerField('Максимальная скорость', null=True)
    acceleration = DecimalField('Разгон автомобиля', max_digits=3, decimal_places=1, null=True)
    fuel_consumption = CharField('Расход топлива', max_length=50, null=True)
    trunk_volume = CharField('Объем багажника', max_length=20, null=True)
    fuel_tank_volume = IntegerField('Объём топливного бака', null=True)
    curb_weight = IntegerField('Снаряженная масса', null=True)
    full_mass = IntegerField('Полная  масса', null=True)
    torque = CharField('Крутящий момент', null=True)
    number_of_cylinders = IntegerField('Количество цилиндров', null=True)
    number_of_gears = IntegerField('Количество передач', null=True)

    country = ForeignKey('store.Country', verbose_name='Страна марки', on_delete=CASCADE, related_name='car')
    environmental_class = ForeignKey('store.EnvironmentalClass', verbose_name='Экологический класс', on_delete=CASCADE,
                                     related_name='car')
    size = ForeignKey('store.Size', verbose_name='Размеры автомобиля', on_delete=CASCADE, related_name='car')
    drive = ForeignKey('store.Drive', verbose_name='Тип привода', on_delete=CASCADE, related_name='car')
    boost = ForeignKey('store.Boost', verbose_name='Тип наддува', on_delete=CASCADE, related_name='car')
    fuel = ForeignKey('store.Fuel', verbose_name='Тип топлива', on_delete=CASCADE, related_name='car')
    gear = ForeignKey('store.Gear', verbose_name='Вид коробки автомобиля', on_delete=CASCADE, related_name='car')

    class Meta:
        verbose_name = 'Детальные характеристики автомобиля'
        verbose_name_plural = 'Детальные характеристики автомобиля'

    def __str__(self):
        return 'Детальные характеристики автомобиля'
