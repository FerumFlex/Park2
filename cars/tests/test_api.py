import json
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import RequestsClient

from cars.models import Driver, Vehicle
from cars.serializers import DriverSerializer, VehicleSerializer

from django.contrib.auth.models import User


class DriverApiTestCase(APITestCase):
    def setUp(self):

        self.user = User.objects.create(username='test_username')
        self.driver_1 = Driver.objects.create(first_name="fname1", last_name="lname1")
        self.driver_2 = Driver.objects.create(first_name="fname2", last_name="lname2")
        self.driver_3 = Driver.objects.create(first_name="fname3", last_name="lname3")

    def test_get_driver(self):
        response = self.client.get('/drivers/driver/', follow=True)
        serializer_data = DriverSerializer([self.driver_1, self.driver_2, self.driver_3], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_filter(self):
        response = self.client.get('/drivers/driver/', follow=True,
                                   data={"created_at": 'created_at__gte'})
        serializer_data = DriverSerializer([self.driver_1, self.driver_2, self.driver_3], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_create(self):
        self.assertEqual(3, Driver.objects.all().count())
        data = {
            "first_name": "Firstname",
            "last_name": "Lastname"
        }
        response = self.client.post('/drivers/driver/', data=data, format="json")
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(4, Driver.objects.all().count())

    def test_update(self):
        data = {
            "first_name": "Firstname",
            "last_name": "Lastname"
        }
        self.client.force_login(self.user)
        response = self.client.put('/drivers/driver/3/', data=data, format="json")
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.driver_3.refresh_from_db()
        self.assertEqual(data["first_name"], self.driver_3.first_name)

    def test_delete(self):

        self.client.force_login(self.user)
        response = self.client.delete('/drivers/driver/1/', follow=True)
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
        self.assertEqual(2, Driver.objects.all().count())

