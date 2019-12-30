from rest_framework import serializers

from dcim.api.nested_serializers import NestedDeviceSerializer
from ..models import DeviceExample, Example


#
# Examples
#

class ExampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Example
        fields = ['id', 'name', 'value']


class DeviceExampleSerializer(serializers.ModelSerializer):
    device = NestedDeviceSerializer()

    class Meta:
        model = DeviceExample
        fields = ['id', 'device', 'name', 'value']
