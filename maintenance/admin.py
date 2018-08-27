from django.contrib import admin

# Register your models here.

from .models import Device, Device_type, Maintenance
# Register your models here.

admin.site.register(Maintenance)
admin.site.register(Device)
admin.site.register(Device_type)
