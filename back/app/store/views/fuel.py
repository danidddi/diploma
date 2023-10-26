from rest_framework.viewsets import ModelViewSet

from store.models import Fuel
from store.serializers import FuelSerializer


class FuelViewSet(ModelViewSet):
    queryset = Fuel.objects.all()
    serializer_class = FuelSerializer
