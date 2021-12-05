from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from cars.models import Vehicle, Driver
from cars.serializers import VehicleSerializer, DriverSerializer


class VehicleTestCases(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='test_username')
        self.driver_1 = Driver.objects.create(first_name="fname1", last_name="lname1")
        self.driver_2 = Driver.objects.create(first_name="fname2", last_name="lname2")
        self.driver_3 = Driver.objects.create(first_name="fname3", last_name="lname3")

        self.vehicle_1 = Vehicle.objects.create(
            driver=self.driver_1,
            make="test_brand",
            model='test_model',
            plate_number='test_number_1',
        )
        self.vehicle_2 = Vehicle.objects.create(
            driver=self.driver_2,
            make="test_brand",
            model='test_model',
            plate_number='test_number_2',
        )
        self.vehicle_3 = Vehicle.objects.create(
            driver=self.driver_2,
            make="test_brand",
            model='test_model',
            plate_number='test_number_3',
        )

    def test_count(self):
        self.assertEqual(3, Vehicle.objects.all().count())

    def test_get_vehicle(self):
        response = self.client.get(reverse('vehicle-list'))
        serializer_data = VehicleSerializer([self.vehicle_1, self.vehicle_2, self.vehicle_3], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    # def test_create(self):
    #
    #     data = {
    #         "driver": self.driver_1,
    #         "make": "test_brand",
    #         "model": "test_model",
    #         "plate_number": "test_number_4",
    #     }
    #
    #     response = self.client.post('/vehicles/vehicle/', data=data, format="json")
    #     print(response.json())
    #     self.assertEqual(status.HTTP_201_CREATED, response.status_code)
    #     self.assertEqual(4, Vehicle.objects.all().count())
    #     self.assertEqual(data["plate_number"], Vehicle.objects.all()[3].plate_number)

    def test_create_no_driver(self):
        data = {
            "driver": None,
            "make": "test_brand",
            "model": "test_model",
            "plate_number": "test_number_4",
        }

        response = self.client.post('/vehicles/vehicle/', data=data, format="json")
        print(response.json())
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(4, Vehicle.objects.all().count())
        self.assertEqual(data["plate_number"], Vehicle.objects.all()[3].plate_number)

    def test_create_same_number(self):
        data = {
            "driver": None,
            "make": "test_brand",
            "model": "test_model",
            "plate_number": "test_number_3",
        }

        response = self.client.post('/vehicles/vehicle/', data=data, format="json")
        print(response.json())
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)
        self.assertEqual(3, Vehicle.objects.all().count())
# {'plate_number': ['Автомобиль с таким Номерной знак уже существует.']}  как отловить эту ошибку?

#     def test_update(self):
#         data = {
#             "first_name": "Firstname",
#             "last_name": "Lastname"
#         }
#         self.client.force_login(self.user)
#         response = self.client.put('/drivers/driver/3/', data=data, format="json")
#         self.assertEqual(status.HTTP_200_OK, response.status_code)
#         self.driver_3.refresh_from_db()
#         self.assertEqual(data["first_name"], self.driver_3.first_name)
#         self.assertEqual(data["last_name"], self.driver_3.last_name)
#
#     def test_delete(self):
#         self.client.force_login(self.user)
#         response = self.client.delete(reverse('driver-detail', kwargs={'pk': 2}))
#         self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
#         self.assertEqual(2, Driver.objects.all().count())
#
#     def test_filter(self):
#         response = self.client.get('/drivers/driver/', follow=True,
#                                    data={"created_at": 'created_at__gte'})
#         serializer_data = DriverSerializer([self.driver_1, self.driver_2, self.driver_3], many=True).data
#         self.assertEqual(status.HTTP_200_OK, response.status_code)
#         self.assertEqual(serializer_data, response.data)
#
#     def test_fail_driver_detail(self):
#         response = self.client.get(reverse('driver-detail', kwargs={'pk': 10}))
#         self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)
#
#     def test_driver_detail(self):
#         response = self.client.get(reverse('driver-detail', kwargs={'pk': self.driver_3.id}))
#         self.assertEqual(status.HTTP_200_OK, response.status_code)
#         self.assertEqual(response.json().get('first_name'), "fname3")
#         self.assertEqual(response.json().get('last_name'), "lname3")
#
#     def test_driver_list(self):
#         response = self.client.get(reverse('driver-list'))
#         # serializer_data = DriverSerializer([self.driver_1, self.driver_2, self.driver_3], many=True).data
#         self.assertEqual(status.HTTP_200_OK, response.status_code)
#         self.assertTrue({'id': 1, 'first_name': 'fname1', 'last_name': 'lname1'} in response.json())
