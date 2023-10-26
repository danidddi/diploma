from rest_framework.serializers import ModelSerializer

from store.models import Bid


class BidSerializer(ModelSerializer):
    class Meta:
        model = Bid
        fields = '__all__'
