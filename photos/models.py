from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class AbstractLocation(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Название',
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
        max_length=255,
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True,
        null=True
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Владелец',
        null=True,
        blank=True
    )

    class Meta:
        abstract = True


class Item(AbstractThing):
    class Meta:
        default_related_name = 'items'
        verbose_name = 'Вещь'
        verbose_name_plural = 'Вещи'

    def __str__(self):
        return self.title


class Country(AbstractLocation):
    GOVERNMENT_TYPES = (
        'absolute_monarchy', 'constitutional_monarchy', 'dualistic_monarchy', 'parliament_monarchy',
        'president_republic', 'parliament_republic', 'mixed_republic'
    )
    GOVERNMENT_TYPES_RU = ('Абсолютная монархия', 'Конституционная монархия', 'Дуалистическая монархия',
                           'Парламентская монархия', 'Президентская республика', 'Парламентская республика',
                           'Смешанная республика')
    CHOICES = tuple(zip(GOVERNMENT_TYPES, GOVERNMENT_TYPES_RU))

    official_language = models.CharField(
        verbose_name='Официальный язык',
        max_length=255
    )
    government_type = models.CharField(
        verbose_name='Форма правления',
        max_length=len(max(GOVERNMENT_TYPES, key=len)),
        choices=CHOICES,
        blank=True,
        null=True
    )
    capital = models.OneToOneField(
        "City",
        on_delete=models.CASCADE,
        verbose_name='Столица',
    )
    currency = models.CharField(
        verbose_name='Валюта',
        max_length=255,
        blank=True,
        null=True
    )

    class Meta:
        default_related_name = 'capital'
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'

    def __str__(self):
        return self.name


class City(AbstractLocation):
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        verbose_name='Страна',
        blank=True,
        null=True
    )
    item = models.ForeignKey(
        Item,
        on_delete=models.SET_NULL,
        verbose_name='Вещь',
        null=True,
        blank=True
    )

    class Meta:
        default_related_name = 'cities'
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
        constraints = [
            models.UniqueConstraint(fields=('name', 'founding_date', 'demonym', 'ruler', 'area', 'population'),
                                    name='unique_city')
        ]

    def __str__(self):
        return self.name


class PhotoManager(models.Manager):
    def approved_photos(self):
        return self.filter(is_approved=True)

    def approved_photos_for_entity(self, entity_type, entity_id):
        if entity_type == 'country':
            return self.filter(country_id=entity_id, is_approved=True)
        elif entity_type == 'city':
            return self.filter(city_id=entity_id, is_approved=True)
        elif entity_type == 'item':
            return self.filter(item_id=entity_id, is_approved=True)
        elif entity_type == 'user':
            return self.filter(user_id=entity_id, is_approved=True)
        else:
            return self.none()

    def unapproved_photos(self):
        return self.filter(is_approved=False)


class Photo(AbstractThing):
    image = models.ImageField(
        verbose_name='Картинка',
        upload_to='photos/images/',
        null=True,
        blank=True
    )
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        verbose_name='Страна',
        null=True,
        blank=True
    )
    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        verbose_name='Город',
        null=True,
        blank=True
    )
    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        verbose_name='Вещь',
        null=True,
        blank=True
    )
    is_approved = models.BooleanField(
        default=True,
        verbose_name='Одобрено администратором'
    )

    photos_manager = PhotoManager()

    class Meta:
        default_related_name = 'photos'
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'

    def __str__(self):
        return self.title
