from .models import Driver
from rest_framework import viewsets, permissions

from .serializers import DriverSerializer


class DriverViewSet(viewsets.ModelViewSet):
    """Перечень водителей"""
    queryset = Driver.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = DriverSerializer
