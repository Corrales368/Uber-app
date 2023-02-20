# Import django
from rest_framework import serializers

# Import self app
from ..models import DriverLocation


class DriverLocationSerializer(serializers.ModelSerializer):
    """
    Serializer to validate latitude and longitude to store a new location
    """
    latitude = serializers.DecimalField(max_digits=30, decimal_places=27)
    longitude = serializers.DecimalField(max_digits=30, decimal_places=27)
    class Meta:
        model = DriverLocation
        fields = [
            'latitude',
            'longitude',
        ]

    def validate_latitude(self, value):
        if value > 90 or value < -90:
            raise serializers.ValidationError("Latitude must be between -90 and 90")
        return round(value, 6)

    def validate_longitude(self, value):
        if value > 180 or value < -180:
            raise serializers.ValidationError("Longitude must be between -180 and 180")
        return round(value, 6)
    
    
