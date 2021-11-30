from .models import Driver, Vehicle
from rest_framework import viewsets, permissions
from .serializers import DriverSerializer
from rest_framework import generics
from django_filters import rest_framework as filters
import django_filters


class DriverDateFilter(django_filters.FilterSet):
    created_at__gte = django_filters.DateFilter(field_name="created_at", lookup_expr='gte', input_formats=["%d-%m-%Y"])
    created_at__lte = django_filters.DateFilter(field_name="created_at", lookup_expr='lte', input_formats=["%d-%m-%Y"])

    class Meta:
        model = Driver
        # start_time = serializers.DateField(format="%d/%m/%Y %H:%M:%S")
        fields = ['created_at__gte', 'created_at__lte']


class DriverViewSet(viewsets.ModelViewSet):
    """Перечень водителей"""
    queryset = Driver.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = DriverSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = DriverDateFilter



