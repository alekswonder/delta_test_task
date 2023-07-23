from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ItemViewSet, CountryViewSet, CityViewSet, PhotoViewSet

router = DefaultRouter()

router.register(r'items', ItemViewSet, basename='items')
router.register(r'countries', CountryViewSet, basename='country')
router.register(r'cities', CityViewSet, basename='city')
router.register(r'photos', PhotoViewSet, basename='photo')

urlpatterns = [
    path('', include(router.urls))
]
