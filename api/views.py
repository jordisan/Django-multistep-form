from rest_framework import viewsets

from general.models.customer import Customer
from .serializers import CustomerSerializer

class CustomerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    lookup_field = 'email'
    lookup_value_regex = '[^/]+'