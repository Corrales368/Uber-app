# Import django
from rest_framework import serializers
from django.forms.models import model_to_dict
from django.conf import settings

# Import project apps
from apps.geolocation.utils import GeoLocationGMaps

# Import self app
from ..models import Service


class ServiceSerializer(serializers.ModelSerializer):
    """
    Serializer for model service
    """
    class Meta:
        model = Service
        fields = [
            'client',
            'driver',
            'pickup_latitude',
            'pickup_longitude',
            'destination_latitude',
            'destination_longitude',
            'pickup_time',
            'status',
        ]

    def call_api(self, pickup_lat, pickup_lng, dest_lat, dest_lng):
        """
        Call Google Maps API y create object gmaps
        """
        gmaps = GeoLocationGMaps()
        gmaps.get_matrix_from_coords(pickup_lat, pickup_lng, dest_lat, dest_lng)
        self.distance = gmaps.get_distance
        self.duration = gmaps.get_duration

    def get_distance_between_pickup_and_destination(self):
        """
        Get distance between two points as coordinates
        """
        if self.distance is None:
            raise serializers.ValidationError('Error getting distance')
        return self.distance
    
    def get_duration_between_pickup_and_destination(self):
        """
        Get distance between two points as coordinates
        """
        if self.duration is None:
            raise serializers.ValidationError('Error getting duration')
        return self.duration

    def get_fare(self):
        """
        Get the rate according to the distance
        """
        distance = self.get_distance_between_pickup_and_destination()
        duration = self.get_duration_between_pickup_and_destination()
        print(distance, duration)
        fare_by_duration = (duration / 60) * settings.COST_PER_MINUTE
        fare_by_distance = (distance / 100) * settings.COST_PER_100_METERS
        fare = fare_by_duration + fare_by_distance
        return fare
        
    def create(self, validated_data):
        client = validated_data['client']
        # If a service of client is active, then raise error
        if Service.objects.get_service_active(client):
            raise serializers.ValidationError('You already have an active service.')
        
        # Call API
        self.call_api(
            # Get pickup coordinates
            validated_data['pickup_latitude'],
            validated_data['pickup_longitude'],
            # Get destination coordinates
            validated_data['destination_latitude'],
            validated_data['destination_longitude']
        )
        
        # Get distance 
        validated_data['distance'] = self.distance

        # Get fare
        validated_data['fare'] = self.get_fare()
        return super().create(validated_data)

    def to_representation(self, instance):
        data = model_to_dict(instance)
        data['distance'] = str(instance.distance)
        data['status'] = str(instance.get_status_display())
        return data
    