import django_filters

from .models import DeviceExample, Example


class ExampleFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        field_name='name',
        lookup_expr='icontains',
    )

    class Meta:
        model = Example
        fields = ['id', 'name']


class DeviceExampleFilter(django_filters.FilterSet):
    device = django_filters.CharFilter(
        field_name='device__name',
        lookup_expr='icontains',
    )
    name = django_filters.CharFilter(
        field_name='name',
        lookup_expr='icontains',
    )

    class Meta:
        model = DeviceExample
        fields = ['id', 'device', 'name']
