from rest_framework.viewsets import ModelViewSet
from store.models import Boost
from store.serializers import BoostSerializer


class BoostViewSet(ModelViewSet):
    queryset = Boost.objects.all()
    serializer_class = BoostSerializer
