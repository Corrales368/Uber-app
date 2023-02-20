# Import django
from django.db import models

# Import project apps
from apps.client.models import Client
from apps.driver.models import Driver

# Import self app
from . import choices


class Service(models.Model):
    """
    Model to store service
    """
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, null=True, blank=True)
    pickup_latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    pickup_longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    destination_latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    destination_longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    pickup_time = models.DateTimeField()
    status = models.IntegerField(choices=choices.STATUS_SERVICES)
    fare = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    distance = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f"Service {self.pk} - Client: {self.client} - Driver: {self.driver} - Status: {self.get_status_display()}"

