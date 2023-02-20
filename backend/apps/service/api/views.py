# Import django
from rest_framework import viewsets
from rest_framework import generics

# Import self app
from apps.service.models import Service
from .serializers import ServiceSerializer


class ServiceModelViewSet(viewsets.ModelViewSet):
    """
    Modelviewset for service with CRUD operations generics
    """
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()