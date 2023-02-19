# Import django
from django.urls import path

# Import self app
from .views import GeolocationAPIView


urlpatterns = [
    path('api/v1/geolocation/', GeolocationAPIView.as_view(), name='geolocationapiview'),
]
