from rest_framework import routers
from .views import DriverViewSet, VehicleViewSet, VehicleDriverView
from django.urls import path
from cars import views

router = routers.DefaultRouter()
router.register('drivers/driver', DriverViewSet, 'driver')
router.register('vehicles/vehicle', VehicleViewSet, 'vehicle')
# router.register('vehicles/vehicle/driver', VehicleDriverView, 'vehicle')


urlpatterns = [
    path('drivers/driver/<int:pk>/', views.VehicleDriverView.as_view()),
]


urlpatterns += router.urls

