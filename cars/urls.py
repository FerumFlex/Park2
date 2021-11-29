from rest_framework import routers
from .views import DriverViewSet


router = routers.DefaultRouter()
router.register('view/driver', DriverViewSet, 'driver')

urlpatterns = router.urls

