# Import django
from rest_framework.routers import DefaultRouter

# Import self app
from .views import ServiceModelViewSet


router = DefaultRouter()

router.register('api/v1/service', ServiceModelViewSet, basename='service')

urlpatterns = router.urls
