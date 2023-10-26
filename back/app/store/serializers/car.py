from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from store.models import Car, Image
from store.serializers import CharacteristicsSerializer, BrandSerializer, CarBodySerializer, ColorSerializer, \
    ImageSerializer


class CarSerializer(ModelSerializer):
    characteristics = CharacteristicsSerializer()
    brand = BrandSerializer()
    car_body = CarBodySerializer()
    exterior_color = ColorSerializer()

    images = ImageSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(allow_empty_file=False, use_url=False),
        write_only=True
    )

    class Meta:
        model = Car
        fields = '__all__'

    def create(self, validated_data):
        uploaded_images = validated_data.pop("uploaded_images")
        car = Car.objects.create(**validated_data)

        for image in uploaded_images:
            Image.objects.create(car=car, image=image)

        return car
