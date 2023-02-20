# Import django
from django.urls import path

# Import self app
from .views import LastLocationDriver


urlpatterns = [
    path('api/v1/driver/location/last-location', LastLocationDriver.as_view(), name='last-location'),
]
