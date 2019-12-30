from django.db import models

from dcim.models import Device


class Example(models.Model):
    name = models.CharField(max_length=50, unique=True)
    value = models.CharField(max_length=100)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class DeviceExample(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    value = models.TextField(blank=True)

    class Meta:
        ordering = ('device__name', 'name')
        unique_together = (
            ('device', 'name'),
        )

    def __str__(self):
        return "{} - {}".format(self.device.name, self.name)
