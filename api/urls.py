from django.urls import include, path
from rest_framework import routers
from .views import CustomerViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'customers', CustomerViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]