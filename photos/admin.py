from django.contrib import admin
from django.contrib.auth import get_user_model

from photos.models import Country, City, Item, Photo


admin.site.register(Country)
admin.site.register(City)
admin.site.register(Item)
admin.site.register(Photo)
