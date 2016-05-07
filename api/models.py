from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Organization(models.Model):
    def __str__(self):
        return 'Кредитная организация'

    created = models.DateTimeField(name='Создано')
    changed = models.DateTimeField(name='Изменено')
    name = models.TextField(name='название')


class Credit(models.Model):
    def __str__(self):
        return 'Кредитное дело'

    created = models.DateTimeField(verbose_name='Создано')
    changed = models.DateTimeField(verbose_name='Изменено')
    fio = models.TextField(verbose_name='Фамилия, имя, отчество должника')
    birth_date = models.DateField(verbose_name='Дата рождения')
    debt = models.DecimalField(verbose_name='Долг', decimal_places=2, max_digits=10)
    passport = models.TextField(verbose_name='Номер пасспорта')  # TODO Validators
    organization = models.ForeignKey(
        Organization,
        verbose_name='Кредитная организация',
        on_delete=models.CASCADE
    )
    status = models.TextField(
        verbose_name='Статус',
        choices=(
            ('new', 'новое'),
            ('processing', 'в работе'),
            ('processed', 'не в работе')
        )
    )
    partner = models.ForeignKey(User, verbose_name='Партнёр, взявший в работу')