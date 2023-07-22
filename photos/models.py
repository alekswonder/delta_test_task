from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class AbstractLocation(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Название'
    )
    founding_date = models.DateField(
        verbose_name='Дата основания'
    )
    demonym = models.CharField(
        max_length=255,
        verbose_name='Название жителей',
        blank=True,
        null=True
    )
    ruler = models.CharField(
        max_length=255,
        verbose_name='Под управлением'
    )
    area = models.IntegerField(
        verbose_name='Площадь'
    )
    population = models.IntegerField(
        verbose_name='Количество жителей'
    )

    class Meta:
        abstract = True


class AbstractThing(models.Model):
    title = models.CharField(
        verbose_name='Название',
        max_length=255
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True,
        null=True
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        verbose_name='Владелец'
    )

    class Meta:
        abstract = True


class Item(AbstractThing):
    class Meta:
        default_related_name = 'items'
        verbose_name = 'Вещь'
        verbose_name_plural = 'Вещи'


class Country(AbstractLocation):
    official_language = models.CharField(
        verbose_name='Официальный язык',
        max_length=255
    )
    government_type = models.CharField(
        verbose_name='Тип правления',
        max_length=255
    )
    capital = models.OneToOneField(
        "City",
        on_delete=models.CASCADE,
        verbose_name='Столица'
    )
    currency = models.CharField(
        verbose_name='Валюта',
        max_length=255,
    )

    class Meta:
        default_related_name = 'country'
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'


class City(AbstractLocation):
    country = models.ForeignKey(
        Country,
        on_delete=models.SET_NULL,
        verbose_name='Страна'
    )
    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        verbose_name='Вещь'
    )

    class Meta:
        default_related_name = 'cities'
        verbose_name = 'Город'
        verbose_name_plural = 'Города'


class Photo(AbstractThing):
    image = models.ImageField(
        verbose_name='Картинка',
        upload_to='photos/'
    )
    country = models.ForeignKey(
        Country,
        on_delete=models.SET_NULL,
        verbose_name='Страна'
    )
    city = models.ForeignKey(
        City,
        on_delete=models.SET_NULL,
        verbose_name='Город'
    )
    item = models.ForeignKey(
        Item,
        on_delete=models.SET_NULL,
        verbose_name='Вещь'
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        verbose_name='Владелец'
    )
    is_approved = models.BooleanField(
        default=True,
        verbose_name=''
    )

    class Meta:
        default_related_name = 'photos'
