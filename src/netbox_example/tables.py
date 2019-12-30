from django_tables2 import LinkColumn, TemplateColumn

from utilities.tables import BaseTable, ToggleColumn
from .models import DeviceExample, Example


#
# Examples
#

class ExampleTable(BaseTable):
    pk = ToggleColumn()
    actions = TemplateColumn(
        template_name='netbox_example/example_buttons.html',
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
    device = LinkColumn()
    actions = TemplateColumn(
        template_name='netbox_example/deviceexample_buttons.html',
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
