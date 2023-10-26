from django.urls import path
from rest_framework.routers import DefaultRouter

from favorites.views import FavoritesViewSet

router = DefaultRouter()

urlpatterns = router.urls

urlpatterns.extend([
    path('favorites', FavoritesViewSet.as_view({
        'get': 'list'
    })),
])
