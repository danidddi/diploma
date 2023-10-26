from rest_framework.serializers import ModelSerializer

from store.models import Drive


class DriveSerializer(ModelSerializer):
    class Meta:
        model = Drive
        fields = '__all__'
