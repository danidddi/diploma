from rest_framework.viewsets import ModelViewSet
from store.models import Gear
from store.serializers import GearSerializer


class GearViewSet(ModelViewSet):
    queryset = Gear.objects.all()
    serializer_class = GearSerializer
