from rest_framework.viewsets import ModelViewSet
from store.models import Drive
from store.serializers import DriveSerializer


class DriveViewSet(ModelViewSet):
    queryset = Drive.objects.all()
    serializer_class = DriveSerializer
