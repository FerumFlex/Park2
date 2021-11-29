from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render


# Так выводит кирилические имена в 16ти битном коде
# def json_driver(request):
#     data = list(Driver.objects.values())
#     return JsonResponse(data, safe=False)
#
## def json_vehicle(request):
#     data = list(Vehicle.objects.values())
#     return JsonResponse(data, safe=False)
from cars.models import Vehicle


def json_driver(request):
    data = Vehicle.objects.all()
    json_data = serializers.serialize('json', data)
    return HttpResponse(json_data, content_type='application/json')


 # dumpdata --exclude auth.permission --exclude contenttypes --indent 2 --format=json-no-uescape > db.json

 # python .\manage.py dumpdata cars.driver cars.vehicle --indent 2 > db.json

 # python .\manage.py loaddata db.json



