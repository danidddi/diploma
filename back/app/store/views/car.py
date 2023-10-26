from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet

from store.models import Car
from store.serializers import CarSerializer


class CarViewSet(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['brand', 'car_body', 'exterior_color', 'characteristics__fuel']
    search_fields = ['model', 'brand__title', 'car_body__title', 'exterior_color__title', 'characteristics__fuel__title'
                     , 'year', 'cost', 'characteristics__horse_powers', 'characteristics__gear__title']
    ordering_fields = ['brand', 'year', 'cost', 'horse_powers']

