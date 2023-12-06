from rest_framework import routers
from .api import EspecialidadViewSet

router = routers.DefaultRouter()

router.register('api/Especalidad', EspecialidadViewSet , basename= 'Especalidad')

urlpatterns = router.urls
