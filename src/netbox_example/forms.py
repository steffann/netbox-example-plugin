from django import forms

from utilities.forms import APISelect, BootstrapMixin
from .models import DeviceExample, Example


class ExampleFilterForm(BootstrapMixin, forms.Form):
    name = forms.CharField(
        required=False,
        label='Name'
    )


class DeviceExampleFilterForm(BootstrapMixin, forms.Form):
    device = forms.CharField(
        required=False,
        label='Device name'
    )
    name = forms.CharField(
        required=False,
        label='Name'
    )


class ExampleForm(BootstrapMixin, forms.ModelForm):
    class Meta:
        model = Example
        fields = [
            'name', 'value',
        ]


class DeviceExampleForm(BootstrapMixin, forms.ModelForm):
    class Meta:
        model = DeviceExample
        fields = [
            'device', 'name', 'value',
        ]
        widgets = {
            'device': APISelect(api_url='/api/dcim/devices/')
        }
