from rest_framework import routers

from . import views


class NetboxExampleRootView(routers.APIRootView):
    """
    Netbox Example API root view
    """
    def get_view_name(self):
        return 'Netbox Example'


router = routers.DefaultRouter()
router.APIRootView = NetboxExampleRootView

# Examples
router.register(r'example', views.ExampleViewSet)
router.register(r'device-example', views.DeviceExampleViewSet)

urlpatterns = router.urls
