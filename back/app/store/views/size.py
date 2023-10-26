from rest_framework.viewsets import ModelViewSet
from store.models import Size
from store.serializers import SizeSerializer


class SizeViewSet(ModelViewSet):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer
