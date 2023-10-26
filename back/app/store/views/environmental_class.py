from rest_framework.viewsets import ModelViewSet
from store.models import EnvironmentalClass
from store.serializers import EnvironmentalClassSerializer


class BoostViewSet(ModelViewSet):
    queryset = EnvironmentalClass.objects.all()
    serializer_class = EnvironmentalClassSerializer
