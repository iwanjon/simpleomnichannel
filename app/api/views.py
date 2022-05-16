from rest_framework import status, generics, viewsets
from .serializers import *
from app.models import *

class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class= CustomerSerializers
    queryset = Customer.objects.all()

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class= OrderSerializers
    queryset = Order.objects.all()