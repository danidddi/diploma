from rest_framework.serializers import ModelSerializer
from favorites.models import Favorites
from store.serializers import CarSerializer


class FavoritesSerializer(ModelSerializer):
    car = CarSerializer()
    class Meta:
        model = Favorites
        fields = ['car']
