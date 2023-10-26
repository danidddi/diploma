from rest_framework.serializers import ModelSerializer

from store.models import EnvironmentalClass


class EnvironmentalClassSerializer(ModelSerializer):
    class Meta:
        model = EnvironmentalClass
        fields = '__all__'
