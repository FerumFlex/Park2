import django_filters
from django import forms
from django_filters import rest_framework as filters
from rest_framework import viewsets, permissions
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView

from distutils.util import strtobool

from .models import Driver, Vehicle
from .serializers import DriverSerializer, VehicleSerializer, VehicleDriverSerializer


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
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter)
    filterset_class = DriverDateFilter
    ordering_fields = ['id', 'first_name', 'last_name', 'created_at', 'updated_at']


class VehicleDriverFilter(django_filters.FilterSet):
    with_drivers = django_filters.TypedChoiceFilter(
        field_name="driver",
        choices=(('yes', 'True'), ('no', 'False'),),
        coerce=strtobool,
        lookup_expr='isnull',
        exclude=True,
    )

    # Entry.objects.get(id__exact=None)
    # Entry.objects.filter(pub_date__isnull=True)

    class Meta:
        model = Vehicle
        fields = ['with_drivers']
        # fields = {'driver': ['isnull'], }

class VehicleViewSet(viewsets.ModelViewSet):
    """Перечень машин"""
    queryset = Vehicle.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = VehicleSerializer
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter)
    filterset_class = VehicleDriverFilter
    ordering_fields = ['id', 'driver', 'make', 'model', 'plate_number', 'created_at', 'updated_at']


class VehicleDriverView(CreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleDriverSerializer
    lookup_url_kwarg = "vehicle_id"
    lookup_field = "id"

    def create(self, request, vehicle_id):
        vehicle = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        vehicle.driver_id = serializer.data["driver"]
        vehicle.save()

        return Response(VehicleSerializer(instance=vehicle).data)

    # @action(methods=['get'], detail=False)
    # def order(self, request):
    #     order = self.get_queryset().order_by('id').last()
    #     serializer = self.get_serializer_class()(order)
    #     return Response(serializer.data)

    # def get_queryset(self):
    #     return Vehicle.objects.filter(driver_id="7")

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

# class ParkViewSet(viewsets.ModelViewSet):
#     """
#     A viewset that provides the standard actions
#     """
#     queryset = Vehicle.objects.all()
#     serializer_class = VehicleSerializer

# @action(detail=True, methods=['put'], name='Change Driver')
# def set_driver(self, request, pk=None):
#     driver_id = self.get_object()
#     serializer = DriverSerializer(data=request.data)
#     if serializer.is_valid():
#         driver_id.set_driver(serializer.validated_data['driver'])
#         driver_id.save()
#         return Response({'status': 'driver set'})
#     else:
#         return Response(serializer.errors,
#                         status=status.HTTP_400_BAD_REQUEST)

# @action(detail=True, methods=['post', 'delete'])
# def unset_driver(self, request, pk=None):

# @password.mapping.delete
# def delete_password(self, request, pk=None):
#     """Delete the user's password."""
