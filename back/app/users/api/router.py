from django.urls import path
from rest_framework.routers import DefaultRouter

from users.views import CustomUserViewSet

router = DefaultRouter()

urlpatterns = router.urls

urlpatterns.extend([
    path('users', CustomUserViewSet.as_view({
        'get': 'list'
    })),
])
