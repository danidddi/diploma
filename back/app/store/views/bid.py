from rest_framework.viewsets import ModelViewSet
from store.models import Bid
from store.serializers import BidSerializer
from  rest_framework.response import Response
from rest_framework import status


class BidViewSet(ModelViewSet):
    queryset = Bid.objects.all()
    serializer_class = BidSerializer

    def create(self, request, *args, **kwargs):
        print(request.data)
        serializer = BidSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
