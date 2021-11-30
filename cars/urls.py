from rest_framework import routers
from .views import DriverViewSet, VehicleViewSet


router = routers.DefaultRouter()
router.register('view/driver', DriverViewSet, 'driver')
router.register('view/vehicle', VehicleViewSet, 'vehicle')

urlpatterns = router.urls

