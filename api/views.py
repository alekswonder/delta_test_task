from photos.models import Item, Country, City, Photo
from rest_framework import viewsets

from .serializers import ItemSerializer, CountrySerializer, CitySerializer, PhotoSerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.photos_manager.approved_photos()
    serializer_class = PhotoSerializer
