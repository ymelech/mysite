from django.db import models

# Create your models here.


class Device_type(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    def toString(self):
        return self.name.__str__

class Device(models.Model):  
    dev_type = models.ForeignKey(Device_type, on_delete=models.CASCADE)
    sn = models.CharField(max_length=100)
    # dev_id = models.CharField(max_length=100)
    manuf_date = models.DateTimeField(auto_now_add=True)
    descr = models.TextField()
    hw_ver = models.CharField(max_length=100)
    sw_ver = models.CharField(max_length=100)
    # add in thumbnail later
    # add in auther later

    def __str__(self):
        return self.dev_type.__str__() + '-' + self.sn
    
    def toString(self):
        return self.dev_type.__str__() + '-' + self.sn
    
    def dev_name_id(self):
        self.dev_id = self.dev_type.__str__() + '-' + self.sn
        return self.toString()

class Maintenance(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    received_at = models.DateTimeField(auto_now_add=False)
    repaired_at =  models.DateTimeField(auto_now_add=False)
    fault = models.TextField()
    description = models.TextField()
    comments = models.TextField()
    def __str__(self):
        return self.device.__str__() + ' - Fault: ' + self.fault + ' - ( ' + self.repaired_at.__str__() + ' ) ' 


