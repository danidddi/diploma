from rest_framework.viewsets import ModelViewSet
from store.models import Characteristics
from store.serializers import CharacteristicsSerializer


class CharacteristicsViewSet(ModelViewSet):
    queryset = Characteristics.objects.all()
    serializer_class = CharacteristicsSerializer
