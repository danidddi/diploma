from rest_framework.viewsets import ModelViewSet

from store.models import CarBody
from store.serializers import CarBodySerializer


class CarBodyViewSet(ModelViewSet):
    queryset = CarBody.objects.all()
    serializer_class = CarBodySerializer
