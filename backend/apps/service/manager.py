# Import django
from django.db import models

# Import self app
from . import choices

class ServiceManager(models.Manager):
    """
    Manager for model service
    """
    def get_service_active(self, client):
        return self.filter(
            client=client,
            status__in=[
                choices.STATUS_SERVICE_UNASSIGNED,
                choices.STATUS_SERVICE_ASSIGNED
            ]
        ).exists()
        