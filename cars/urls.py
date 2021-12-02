from rest_framework import routers
from django.urls import path
from cars import views



router = routers.DefaultRouter()
router.register(r'drivers/driver', views.DriverViewSet, 'driver')
router.register(r'vehicles/vehicle', views.VehicleViewSet, 'vehicle')
# router.register('vehicles/vehicle/driver', VehicleDriverView, 'vehicle')


urlpatterns = [
    path('vehicles/set_driver/<vehicle_id>/', views.VehicleDriverView.as_view()),
]

urlpatterns += router.urls

