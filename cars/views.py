from .models import Driver, Vehicle
from rest_framework import viewsets, permissions
from .serializers import DriverSerializer, VehicleSerializer
from rest_framework import generics
from django_filters import rest_framework as filters
import django_filters


class DriverDateFilter(django_filters.FilterSet):
    created_at__gte = django_filters.DateFilter(field_name="created_at", lookup_expr='gte', input_formats=["%d-%m-%Y"])
    created_at__lte = django_filters.DateFilter(field_name="created_at", lookup_expr='lte', input_formats=["%d-%m-%Y"])

    class Meta:
        model = Driver
        fields = ['created_at__gte', 'created_at__lte']


class DriverViewSet(viewsets.ModelViewSet):
    """Перечень водителей"""
    queryset = Driver.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = DriverSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = DriverDateFilter


class VehicleDateFilter(django_filters.FilterSet):
    created_at__gte = django_filters.DateFilter(field_name="created_at", lookup_expr='gte', input_formats=["%d-%m-%Y"])
    created_at__lte = django_filters.DateFilter(field_name="created_at", lookup_expr='lte', input_formats=["%d-%m-%Y"])
    # with_no_drivers = django_filters(field_name="driver_id", lookup_expr='None')
    class Meta:
        model = Vehicle
        fields = ['created_at__gte', 'created_at__lte']
        # fields = ['created_at__gte', 'created_at__lte', 'with_no_drivers']

class VehicleViewSet(viewsets.ModelViewSet):
    """Перечень машин"""
    queryset = Vehicle.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = VehicleSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = VehicleDateFilter

