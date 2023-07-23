from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (list_unapproved_photos, list_all_approved_photos,
                    list_approved_photos_by_entity, list_approved_photos_by_concrete_entity,
                    list_every_photo_from_given_entity_by_its_name)

urlpatterns = [
    path('photos/unapproved-photos/', list_unapproved_photos),
    path('photos/', list_all_approved_photos),
    path('photos/<str:entity>/', list_approved_photos_by_entity),
    path('photos/<str:entity>/<int:pk>/', list_approved_photos_by_concrete_entity),
    path('photos/<str:entity>/<str:name>/', list_every_photo_from_given_entity_by_its_name)
]
