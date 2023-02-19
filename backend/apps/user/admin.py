# Import django
from django.contrib import admin

# Import self app
from .models import User

admin.site.register(User)
