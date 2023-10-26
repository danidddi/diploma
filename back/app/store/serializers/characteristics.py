from rest_framework.serializers import ModelSerializer

from store.models import Characteristics

from store.serializers import FuelSerializer, SizeSerializer, DriveSerializer, BoostSerializer, GearSerializer, \
    CountrySerializer, EnvironmentalClassSerializer


class CharacteristicsSerializer(ModelSerializer):
    size = SizeSerializer()
    drive = DriveSerializer()
    boost = BoostSerializer()
    fuel = FuelSerializer()
    gear = GearSerializer()
    country = CountrySerializer()
    environmental_class = EnvironmentalClassSerializer()

    class Meta:

        model = Characteristics
        fields = '__all__'
