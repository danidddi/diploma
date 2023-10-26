from rest_framework.serializers import ModelSerializer

from favorites.serializers import FavoritesSerializer
from users.models import CustomUser


class CustomUserSerializer(ModelSerializer):
    favorites = FavoritesSerializer(many=True, read_only=True)
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'birth_date', 'phone', 'favorites']
