from rest_framework.serializers import ModelSerializer

from store.models import CarBody


class CarBodySerializer(ModelSerializer):
    class Meta:
        model = CarBody
        fields = '__all__'
