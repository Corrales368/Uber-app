# Import django
from django.contrib import admin

# Import self app
from .models import Driver

admin.site.register(Driver)
