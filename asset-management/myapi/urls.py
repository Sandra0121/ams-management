
from django.conf.urls import url,include
from . import views  
from rest_framework import routers
from . import views
from django.conf.urls import include


router = routers.DefaultRouter()
router.register(r'assets', views.assetsviewset)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url('', include(router.urls)),
    url('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]