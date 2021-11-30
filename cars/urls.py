from rest_framework import routers
from .views import DriverViewSet, VehicleViewSet


router = routers.DefaultRouter()
router.register('drivers/driver', DriverViewSet, 'driver')
router.register('vehicles/vehicle', VehicleViewSet, 'vehicle')

urlpatterns = router.urls

