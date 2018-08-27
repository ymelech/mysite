from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'maintenance'

urlpatterns = [
    url(r'^device/$', views.DeviceIndexView.as_view(), name='device_list'),
    path('<int:pk>/', views.DeviceDetailView.as_view(), name='device_details'),
    path('device/<int:pk>/maintenance/', views.DeviceMaintenanceView.as_view(), name='maintenance_by_device'),
    url(r'^maintenance/$', views.MaintenanceIndexView.as_view(), name='maintenance_list'),
    path('maintenance/<int:pk>/', views.MaintenanceDetailView.as_view(), name='maintenance_details'),
]