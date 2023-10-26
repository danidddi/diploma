from rest_framework.serializers import ModelSerializer

from store.models import Boost


class BoostSerializer(ModelSerializer):
    class Meta:
        model = Boost
        fields = '__all__'
