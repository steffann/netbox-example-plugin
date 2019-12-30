from django.core.management.base import BaseCommand

from netbox_example.models import Example


class Command(BaseCommand):
    def handle(self, *args, **options):
        for example in Example.objects.select_related('device').all():
            self.stdout.write("{example.device.name} - {example.name}".format(example=example))
