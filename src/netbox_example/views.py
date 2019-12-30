from django.contrib.auth.mixins import PermissionRequiredMixin

from utilities.views import BulkDeleteView, ObjectDeleteView, ObjectEditView, ObjectListView
from . import filters, forms, tables
from .models import DeviceExample, Example


#
# Examples
#

class ExampleListView(PermissionRequiredMixin, ObjectListView):
    permission_required = 'netbox_example.view_example'
    queryset = Example.objects.all()
    filter = filters.ExampleFilter
    filter_form = forms.ExampleFilterForm
    table = tables.ExampleTable
    template_name = 'netbox_example/example_list.html'


class ExampleCreateView(PermissionRequiredMixin, ObjectEditView):
    permission_required = 'netbox_example.add_example'
    model = Example
    model_form = forms.ExampleForm
    template_name = 'netbox_example/example_edit.html'
    default_return_url = 'netbox_example:example_list'


class ExampleEditView(ExampleCreateView):
    permission_required = 'netbox_example.change_example'


class ExampleDeleteView(PermissionRequiredMixin, ObjectDeleteView):
    permission_required = 'netbox_example.delete_example'
    model = Example


class ExampleBulkDeleteView(PermissionRequiredMixin, BulkDeleteView):
    permission_required = 'netbox_example.delete_example'
    queryset = Example.objects.all()
    filter = filters.ExampleFilter
    table = tables.ExampleTable
    default_return_url = 'netbox_example:example_list'


#
# Device Examples
#

class DeviceExampleListView(PermissionRequiredMixin, ObjectListView):
    permission_required = 'netbox_example.view_deviceexample'
    queryset = DeviceExample.objects.prefetch_related('device')
    filter = filters.DeviceExampleFilter
    filter_form = forms.DeviceExampleFilterForm
    table = tables.DeviceExampleTable
    template_name = 'netbox_example/device_example_list.html'


class DeviceExampleCreateView(PermissionRequiredMixin, ObjectEditView):
    permission_required = 'netbox_example.add_deviceexample'
    model = DeviceExample
    model_form = forms.DeviceExampleForm
    template_name = 'netbox_example/device_example_edit.html'
    default_return_url = 'netbox_example:device_example_list'


class DeviceExampleEditView(DeviceExampleCreateView):
    permission_required = 'netbox_example.change_deviceexample'


class DeviceExampleDeleteView(PermissionRequiredMixin, ObjectDeleteView):
    permission_required = 'netbox_example.delete_deviceexample'
    model = DeviceExample


class DeviceExampleBulkDeleteView(PermissionRequiredMixin, BulkDeleteView):
    permission_required = 'netbox_example.delete_deviceexample'
    queryset = Example.objects.prefetch_related('device')
    filter = filters.DeviceExampleFilter
    table = tables.DeviceExampleTable
    default_return_url = 'netbox_example:device_example_list'
