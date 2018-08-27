from django.shortcuts import render, HttpResponse
from django.views import generic

from .models import Device, Maintenance

# Create your views here.

def device_list(request):
    return HttpResponse('Device List')
    # return render(request, 'articles/article_list.html')

class DeviceIndexView(generic.ListView):
    model = Device
    template_name = 'maintenance/device_list.html'
    context_object_name = 'device'

    def get_queryset(self):
            return Device.objects.all().order_by('dev_type', 'sn')

class DeviceDetailView(generic.DetailView):
    model = Device
    template_name = 'maintenance/device_details.html'
    context_object_name = 'device'

class MaintenanceIndexView(generic.ListView):
    model = Maintenance
    template_name = 'maintenance/maintenance_list.html'
    context_object_name = 'maintenance'

    def get_queryset(self):
        return Maintenance.objects.all().order_by('-repaired_at')

class MaintenanceDetailView(generic.DetailView):
    model = Maintenance
    template_name = 'maintenance/maintenance_details.html'
    context_object_name = 'maintenance'

class DeviceMaintenanceView(generic.ListView):
    model = Maintenance
    template_name = 'maintenance/maintenance_list_by_device.html'
    context_object_name = 'maintenance'
    def get_queryset(self):
        return Maintenance.objects.filter(device__id = self.kwargs['pk']).order_by('-repaired_at')