# Import django
from django.contrib import admin

# Import self app
from .models import Client

admin.site.register(Client)
