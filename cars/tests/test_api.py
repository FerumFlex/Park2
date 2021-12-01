import json
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import RequestsClient

from cars.models import Driver, Vehicle
from cars.serializers import DriverSerializer, VehicleSerializer
# from django.contrib.auth.models.User (AbstractUser) import User
from django.contrib.auth.models import User


class DriverApiTestCase(APITestCase):
    def setUp(self):

        self.user = User.objects.create(username='test_username')
        self.driver_1 = Driver.objects.create(first_name="fname1", last_name="lname1")
        self.driver_2 = Driver.objects.create(first_name="fname2", last_name="lname2")
        self.driver_3 = Driver.objects.create(first_name="fname3", last_name="lname3")

    def test_get(self):
        client = RequestsClient()
        response = client.get('http://testserver/drivers/driver')
        assert response.status_code == 200

    def test_get_driver(self):
        response = self.client.get('http://testserver/drivers/driver', follow=True)
        serializer_data = DriverSerializer([self.driver_1, self.driver_2, self.driver_3], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_filter(self):
        response = self.client.get('http://testserver/drivers/driver', follow=True,
                                   data={"created_at": 'created_at__gte'})
        serializer_data = DriverSerializer([self.driver_1, self.driver_2, self.driver_3], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_create(self):
        self.assertEqual(3, Driver.objects.all().count())
        # data = {
        #     "first_name": "Test_first",
        #     "last_name": "Test_last"
        # }
        data = {
                "id": 1,
                "created_at": "02/09/2021 12:10:23",
                "updated_at": "25/11/2021 18:12:30",
                "first_name": "Firstname",
                "last_name": "Lastname"
        }
        json_data = json.dumps(data)
        self.client.force_login(self.user)
        response = self.client.post('http://testserver/drivers/driver', follow=True,
                                    data=json_data, content_type="application/json")
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(4, Driver.objects.all().count())

    def test_update(self):
        # data = {
        #     "first_name": "Testname",
        #     "last_name": "Testname"
        # }
        data = {
            "id": 1,
            "created_at": "02/09/2021 12:10:23",
            "updated_at": "25/11/2021 18:12:30",
            "first_name": "Firstname",
            "last_name": "Lastname"
        }
        json_data = json.dumps(data)
        self.client.force_login(self.user)
        response = self.client.put('http://testserver/drivers/driver/3', follow=True,
                                    data=json_data, content_type="application/json")
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.driver_1.refresh_from_db()
        self.assertEqual('Firstname', self.driver_3.first_name)

    def test_delete(self):

        self.client.force_login(self.user)
        response = self.client.delete('http://testserver/drivers/driver/1', follow=True)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(2, Driver.objects.all().count())