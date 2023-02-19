# Import django
from django.db import models
from django.conf import settings


class Driver(models.Model):
    """
    Model to store driver
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.user}'
