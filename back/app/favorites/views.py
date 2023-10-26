from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet

from favorites.models import Favorites
from favorites.serializers import FavoritesSerializer


class FavoritesViewSet(ModelViewSet):
    queryset = Favorites.objects.all()
    serializer_class = FavoritesSerializer
    filter_backends = [SearchFilter]
    search_fields = ['user__id']
