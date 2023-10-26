from rest_framework.serializers import ModelSerializer

from store.models import Fuel


class FuelSerializer(ModelSerializer):
    class Meta:
        model = Fuel
        fields = '__all__'
