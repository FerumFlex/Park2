from rest_framework import serializers
from .models import Driver, Vehicle


class DriverSerializer(serializers.ModelSerializer):
    """Список водителей"""

    class Meta:
        model = Driver
        fields = ('__all__')


class VehicleSerializer(serializers.ModelSerializer):
    """Список автомобилей"""

    class Meta:
        model = Vehicle
        fields = ('__all__')
