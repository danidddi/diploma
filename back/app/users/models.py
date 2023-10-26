from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import DateField, CharField


class CustomUser(AbstractUser):
    birth_date = DateField('Дата рождения пользователя', default='2000-01-01')
    phone = CharField('Телефонный номер пользователя', max_length=11, blank=True)
