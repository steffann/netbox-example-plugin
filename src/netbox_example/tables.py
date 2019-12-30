import django_tables2 as tables

from utilities.tables import BaseTable, ToggleColumn
from .models import DeviceExample, Example

EXAMPLE_ACTIONS = """
{% if perms.netbox_example.change_example %}
    <a href="{% url 'netbox_example:example_edit' pk=record.pk %}?return_url={{ request.path }}" class="btn btn-xs btn-warning" title="Edit example">
        <i class="glyphicon glyphicon-pencil" aria-hidden="true"></i>
    </a>
{% endif %}
{% if perms.netbox_example.delete_example %}
    <a href="{% url 'netbox_example:example_delete' pk=record.pk %}?return_url={{ request.path }}" class="btn btn-danger btn-xs" title="Delete example">
        <i class="glyphicon glyphicon-trash" aria-hidden="true"></i>
    </a>
{% endif %}
"""

DEVICE_EXAMPLE_ACTIONS = """
{% if perms.netbox_example.change_deviceexample %}
    <a href="{% url 'netbox_example:device_example_edit' pk=record.pk %}?return_url={{ request.path }}" class="btn btn-xs btn-warning" title="Edit device example">
        <i class="glyphicon glyphicon-pencil" aria-hidden="true"></i>
    </a>
{% endif %}
{% if perms.netbox_example.delete_deviceexample %}
    <a href="{% url 'netbox_example:device_example_delete' pk=record.pk %}?return_url={{ request.path }}" class="btn btn-danger btn-xs" title="Delete device example">
        <i class="glyphicon glyphicon-trash" aria-hidden="true"></i>
    </a>
{% endif %}
"""


#
# Examples
#

class ExampleTable(BaseTable):
    pk = ToggleColumn()
    name = tables.Column()
    value = tables.Column()
    actions = tables.TemplateColumn(
        template_code=EXAMPLE_ACTIONS,
        attrs={
            'td': {
                'class': 'text-right noprint'
            }
        },
        verbose_name=''
    )

    class Meta(BaseTable.Meta):
        model = Example
        fields = ('pk', 'name', 'value')


class DeviceExampleTable(BaseTable):
    pk = ToggleColumn()
    device = tables.LinkColumn()
    name = tables.Column()
    actions = tables.TemplateColumn(
        template_code=DEVICE_EXAMPLE_ACTIONS,
        attrs={
            'td': {
                'class': 'text-right noprint'
            }
        },
        verbose_name=''
    )

    class Meta(BaseTable.Meta):
        model = DeviceExample
        fields = ('pk', 'device', 'name')
