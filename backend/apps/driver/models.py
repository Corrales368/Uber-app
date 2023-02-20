# Import django
import datetime
from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Driver(models.Model):
    """
    Model to store driver
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_avalaible = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.user}'


class DriverLocation(models.Model):
    """
    Model to store last know location
    """
    driver = models.OneToOneField(Driver, on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Location for {self.driver} at {datetime.datetime.strftime(self.timestamp,'%Y-%m-%d %H:%M:%S')}"
