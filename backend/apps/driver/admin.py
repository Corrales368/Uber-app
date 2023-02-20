# Import django
from django.contrib import admin

# Import self app
from .models import Driver, DriverLocation

admin.site.register(Driver)
admin.site.register(DriverLocation)