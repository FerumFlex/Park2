from rest_framework import serializers
from .models import Driver, Vehicle


class DriverSerializer(serializers.ModelSerializer):
    """Список водителей"""

    class Meta:
        model = Driver
        fields = ('__all__')


#
# class DriverCreateSerializer(serializers.ModelSerializer):
#     """Добавление нового водителя"""
#
#     class Meta:
#         model = Driver
#         fields = ('__all__')
#
#
# class DriverDeleteSerializer(serializers.ModelSerializer):
#     """Удаление водителя"""
#
#     class Meta:
#         model = Driver
#         fields = ('__all__')
#
#
# class DriverUpdateSerializer(serializers.ModelSerializer):
#     """Обновление водителя"""
#
#     class Meta:
#         model = Driver
#         fields = ('__all__')
#
