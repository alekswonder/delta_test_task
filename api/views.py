from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_403_FORBIDDEN

from photos.models import Item, Country, City, Photo

from .serializers import PhotoSerializer

User = get_user_model()


@api_view(('GET',))
def list_unapproved_photos(request):
    """Отобразить все не одобренные фото (работает только для модераторов и администраторов)"""
    if request.user.is_staff:
        unapproved_photos = Photo.photos_manager.unapproved_photos()
        return Response(PhotoSerializer(unapproved_photos, many=True).data)
    return Response({'message': 'You do not have permissions'})


@api_view(('GET',))
def list_all_approved_photos(request):
    """Отобразить все одобренные фото"""
    approved_photos = Photo.photos_manager.approved_photos()
    return Response(PhotoSerializer(approved_photos, many=True).data, status=HTTP_403_FORBIDDEN)


@api_view(('GET',))
def list_approved_photos_by_entity(request, entity):
    """Отобразить все фото, которые относятся к сущности"""
    approved_photos_by_entity = Photo.photos_manager.approved_photos_for_entity(entity
                                                                                ).prefetch_related('owner', 'country',
                                                                                                   'city', 'item')
    return Response(PhotoSerializer(approved_photos_by_entity, many=True).data)


@api_view(('GET',))
def list_approved_photos_by_concrete_entity(request, entity, pk):
    """Отобразить все фото конкретной сущности"""
    approved_photos_by_concrete_entity = list()
    if entity == 'owners':
        approved_photos_by_concrete_entity = User.objects.get(pk=pk).photos.all()
    elif entity == 'countries':
        approved_photos_by_concrete_entity = Country.objects.get(pk=pk).photos.all()
    elif entity == 'cities':
        approved_photos_by_concrete_entity = City.objects.get(pk=pk).photos.all()
    elif entity == 'items':
        approved_photos_by_concrete_entity = Item.objects.get(pk=pk).photos.all()
    return Response(PhotoSerializer(approved_photos_by_concrete_entity, many=True).data)


@api_view(('GET',))
def list_every_photo_from_given_entity_by_its_name(request, entity, name):
    """Задача, соответсвующая ТЗ, где в зависимости от конкретной сущности,
       нужно получить все относящиеся к ней данные"""
    photos = []
    if entity == 'countries':
        country = Country.objects.get(name=name)
        photos.extend(country.photos.all())
        cities = country.cities.all()
        for city in cities:
            photos.extend(city.photos.all())
        items = []
        for city in cities:
            items.extend(city.items.all())
        for item in items:
            photos.extend(item.photos.all())
    if entity == 'cities':
        city = City.objects.get(name=name)
        photos.extend(city.photos.all())
        items = city.items.all()
        for item in items:
            photos.extend(item.photos.all())
    if entity == 'items':
        item = Item.objects.get(title=name)
        photos.extend(item.photos.all())

    return Response(PhotoSerializer(photos, many=True).data)
