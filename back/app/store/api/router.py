from django.urls import path, re_path
from rest_framework.routers import DefaultRouter

from store.views.brand import BrandViewSet
from store.views.car import CarViewSet
from store.views.car_body import CarBodyViewSet
from store.views.color import ColorViewSet
from store.views.fuel import FuelViewSet
from store.views.bid import BidViewSet

router = DefaultRouter()

urlpatterns = router.urls

urlpatterns.extend([
    path('cars', CarViewSet.as_view({
        'get': 'list'
    })),

    path('bids', BidViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),

    path('cars/<int:pk>', CarViewSet.as_view({
        'get': 'retrieve'
    })),

    path('handbooks/car-bodys', CarBodyViewSet.as_view({
        'get': 'list'
    })),

    path('handbooks/colors', ColorViewSet.as_view({
        'get': 'list'
    })),

    path('handbooks/fuels', FuelViewSet.as_view({
        'get': 'list'
    })),

    path('handbooks/brands', BrandViewSet.as_view({
        'get': 'list',
    })),
])
