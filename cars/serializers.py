from rest_framework import serializers
from .models import Driver, Vehicle


class DriversListSerializer(serializers.ModelSerializer):
    """Список водителей"""

    class Meta:
        model = Driver
        fields = ('first_name', 'last_name')



class DriverCreateSerializer(serializers.ModelSerializer):
    """Добавление нового водителя"""

    class Meta:
        model = Driver
        fields = ('__all__')


class DriverDeleteSerializer(serializers.ModelSerializer):
    """Удаление водителя"""

    class Meta:
        model = Driver
        fields = ('__all__')


class DriverUpdateSerializer(serializers.ModelSerializer):
    """Обновление водителя"""

    class Meta:
        model = Driver
        fields = ('__all__')

