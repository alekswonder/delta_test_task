from django.contrib.auth import get_user_model

from photos.models import Country, City, Item, Photo

from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username',)


class ItemSerializer(serializers.ModelSerializer):
    owner = UserSerializer()

    class Meta:
        model = Item
        fields = ('title', 'description', 'owner')


class CountrySerializer(serializers.ModelSerializer):
    capital = serializers.StringRelatedField(many=False)

    class Meta:
        model = Country
        fields = '__all__'
        lookup_fields = 'slug'
        extra_kwargs = {
            'url': {'lookup_fields': 'slug'}
        }


class CitySerializer(serializers.ModelSerializer):
    country = serializers.StringRelatedField(many=False)
    item = serializers.StringRelatedField(many=False)

    class Meta:
        model = City
        fields = '__all__'
        lookup_fields = 'slug'
        extra_kwargs = {
            'url': {'lookup_fields': 'slug'}
        }


class PhotoSerializer(serializers.ModelSerializer):
    owner = UserSerializer()
    country = CountrySerializer()
    city = CitySerializer()
    item = ItemSerializer()

    class Meta:
        model = Photo
        fields = '__all__'
