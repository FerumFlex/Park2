from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Driver, Vehicle
from rest_framework import viewsets, permissions, request, status
from .serializers import DriverSerializer, VehicleSerializer

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


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class VehicleDriverFilter(django_filters.FilterSet):
    with_drivers = CharFilterInFilter(field_name="driver_id", lookup_expr='isnull')

    class Meta:
        model = Vehicle
        fields = ['with_drivers']


class VehicleViewSet(viewsets.ModelViewSet):
    """Перечень машин"""
    queryset = Vehicle.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = VehicleSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = VehicleDriverFilter


# class VehicleDriversList(generics.ListAPIView):
#     serializer_class = VehicleSerializer
#
#     def get_queryset(self):
#         """Отбор машин по наличию водителя"""
#         queryset = Vehicle.objects.all()
#         driver_id = self.request.query_params.get('driver_id')
#         if driver_id is None:
#             queryset = queryset.filter(vehicle__driver_id=driver_id)
#         return queryset

class ParkViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions
    """
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

    @action(detail=True, methods=['put'], name='Change Driver')
    def set_driver(self, request, pk=None):
        driver_id = self.get_object()
        serializer = DriverSerializer(data=request.data)
        if serializer.is_valid():
            driver_id.set_driver(serializer.validated_data['driver'])
            driver_id.save()
            return Response({'status': 'driver set'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    # @action(detail=True, methods=['post', 'delete'])
    # def unset_driver(self, request, pk=None):

    # @password.mapping.delete
    # def delete_password(self, request, pk=None):
    #     """Delete the user's password."""
