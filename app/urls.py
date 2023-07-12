from __future__ import annotations

from django.urls import include
from django.urls import path
from rest_framework import routers

from app.core import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path('', include(router.urls)),
    path(
        'api-auth/', include(
            'rest_framework.urls',
            namespace='rest_framework',
        ),
    ),
]
