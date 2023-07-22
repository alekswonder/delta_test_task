from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Country(models.Model):
    ...

    class Meta:
        ...


class City(models.Model):
    country = models.ForeignKey(
        Country,
        ...
    )

    class Meta:
        default_related_name = 'cities'


class Item(models.Model):
    ...


class Photo(models.Model):
    country = models.ForeignKey(
        Country,
        ...
    )
    city = models.ForeignKey(
        City,
        ...
    )
    item = models.ForeignKey(
        Item,
        ...
    )
    owner = models.ForeignKey(
        User,
        ...
    )

    class Meta:
        default_related_name = 'photos'
