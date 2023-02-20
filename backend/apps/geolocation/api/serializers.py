# Import django
from rest_framework import serializers

# Import self app
from ..utils import GeoLocationGMaps


class AddressGeolocationSerializer(serializers.Serializer):
    """
    Serializer for validating an address and returning its geolocation.
    """
    address = serializers.CharField(max_length=255)

    def validate_address(self, value):
        # Get geocode address
        gmaps = GeoLocationGMaps()
        gmaps.get_distance_matrix_from_coords(lat1=6.3237537, lng1=-75.55857870000001, lat2=6.3444097 , lng2=-75.5587506)
        geocode_result = gmaps.get_geocode_from_address(address= value)

        # If geocode_result is empty, then raise error
        if not geocode_result:
            raise serializers.ValidationError("Invalid address")

        # Get location from api, and store object and don't make 2 api calls
        self.geocode = geocode_result[0]['geometry']['location']
        return value

    def to_representation(self, instance):
        # Get geocode from validate address
        geocode = self.geocode
        return {'lat': geocode['lat'], 'lng': geocode['lng']}
