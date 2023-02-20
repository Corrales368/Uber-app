# Import django
from django.contrib import admin

# Import self app
from .models import Service

admin.site.register(Service)

