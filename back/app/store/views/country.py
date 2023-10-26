from rest_framework.viewsets import ModelViewSet
from store.models import Country
from store.serializers import CountrySerializer


class CountryViewSet(ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
