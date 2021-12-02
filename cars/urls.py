from rest_framework import routers
from .views import DriverViewSet, VehicleViewSet, VehicleDriverView


router = routers.DefaultRouter()
router.register('drivers/driver', DriverViewSet, 'driver')
router.register('vehicles/vehicle', VehicleViewSet, 'vehicle')
router.register('vehicles/vehicle/driver', VehicleDriverView, 'vehicle')

urlpatterns = router.urls

