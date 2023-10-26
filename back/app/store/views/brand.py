from rest_framework.viewsets import ModelViewSet
from store.models import Brand
from store.serializers import BrandSerializer
from  rest_framework.response import Response
from rest_framework import status


class BrandViewSet(ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
