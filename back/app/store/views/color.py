from rest_framework.viewsets import ModelViewSet

from store.models import Color
from store.serializers import ColorSerializer


class ColorViewSet(ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
