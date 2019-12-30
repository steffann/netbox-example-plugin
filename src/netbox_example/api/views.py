from utilities.api import ModelViewSet
from . import serializers
from .. import filters
from ..models import DeviceExample, Example


#
# Examples
#

class ExampleViewSet(ModelViewSet):
    queryset = Example.objects.all()
    serializer_class = serializers.ExampleSerializer
    filterset_class = filters.ExampleFilter


class DeviceExampleViewSet(ModelViewSet):
    queryset = DeviceExample.objects.all()
    serializer_class = serializers.DeviceExampleSerializer
    filterset_class = filters.DeviceExampleFilter
