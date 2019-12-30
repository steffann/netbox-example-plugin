import django_filters

from extras.filters import CreatedUpdatedFilterSet
from .models import Example


class ExampleFilter(CreatedUpdatedFilterSet):
    name = django_filters.CharFilter(
        field_name='name',
        lookup_expr='icontains',
        label='Example',
    )

    class Meta:
        model = Example
        fields = ['id', 'name']


class DeviceExampleFilter(CreatedUpdatedFilterSet):
    device = django_filters.CharFilter(
        field_name='device__name',
        lookup_expr='icontains',
        label='Device',
    )
    name = django_filters.CharFilter(
        field_name='name',
        lookup_expr='icontains',
        label='Example',
    )

    class Meta:
        model = Example
        fields = ['id', 'device', 'name']
