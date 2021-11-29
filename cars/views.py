import datetime

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Driver
from .serializers import DriversListSerializer, DriverCreateSerializer


class DriverListView(APIView):
    """Перечень водителей"""

    def get(self, request):
        drivers = Driver.objects.all()
        serializer = DriversListSerializer(drivers, many=True)
        return Response(serializer.data)


class PastDriverListView(APIView):
    """Перечень водителей, которые созданы после 10.11.2021"""

    def get(self, request):
        drivers = Driver.objects.filter(created_at__date__gte=datetime.date(2021, 11, 10))
        serializer = DriversListSerializer(drivers, many=True)
        return Response(serializer.data)


class BeforeDriverListView(APIView):
    """Перечень водителей, которые созданы до 16.11.2021"""

    def get(self, request):
        drivers = Driver.objects.filter(created_at__date__lte=datetime.date(2021, 11, 16))
        serializer = DriversListSerializer(drivers, many=True)
        return Response(serializer.data)


class ThisDriverListView(APIView):
    """Информация по водителю"""

    def get(self, request, pk):
        driver = Driver.objects.get(id=pk)
        serializer = DriversListSerializer(driver)
        return Response(serializer.data)


class DriverCreateView(APIView):
    """Добавление нового водителя"""

    def post(self, request):
        driver = DriverCreateSerializer(data=request.data)
        if driver.is_valid():
            driver.save()
        return Response(status=201)


class DriverDeleteView(APIView):
    """Удаление водителя"""

    def delete(self, request, pk):
        driver = Driver.objects.get(id=pk)
        driver.delete()
        return Response(status=201)


class DriverUpdateView(APIView):
    """Обновление водителя"""

    def post(self, request, pk, instance, validated_data):
        driver = Driver.objects.get(id=pk)

        first_name = validated_data.get("first_name", instance.first_name),
        last_name = validated_data.get("last_name", instance.last_name),
        instance.first_name = first_name
        instance.last_name = last_name
        instance.save()
        return instance
