from django.urls import path

from cars import views

urlpatterns = [
    path('drivers/driver/', views.DriverListView.as_view()),
    path('drivers/driver/create_at__gte=10-11-2021/', views.PastDriverListView.as_view()),
    path('drivers/driver/create_at__gte=16-11-2021/', views.BeforeDriverListView.as_view()),
    path('drivers/driver/<int:pk>/', views.ThisDriverListView.as_view()),
    path('drivers/driver/new/', views.DriverCreateView.as_view()),
    path('drivers/driverupdate/<int:pk>/', views.DriverUpdateView.as_view()),
    path('drivers/driverdel/<int:pk>/', views.DriverDeleteView.as_view()),
]

