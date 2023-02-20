# Import third apps
import os
import googlemaps 


class GeoLocationGMaps:
    """
    Google maps geolocation services 
    """
    def __init__(self):
        # Create instance Google Maps
        self.gmaps = googlemaps.Client(key=os.getenv('GOOGLE_MAPS_API_KEY'))
    
    def get_geocode_from_address(self, address:str):
        """
        Get latitude and longitude from address.
        """
        try:
            # Get coordinates from address as string format
            geocode_result = self.gmaps.geocode(address)
            return geocode_result
        except Exception as e:
            # handle the exception
            print(f"An error occurred: {e}")
            return None

    def get_distance_matrix_from_coords(self, lat1, lng1, lat2, lng2):
        """
        Get distance and duration from origin coordinates to destination coordinates
        """
        try:
            # Define origin and destination coordinates
            origin = f"{lat1},{lng1}"
            destination = f"{lat2},{lng2}"

            # Get distance matrix 
            distance_matrix = self.gmaps.distance_matrix(origin, destination)

            # Extract distance and duration from response
            distance = distance_matrix['rows'][0]['elements'][0]['distance']['value']
            duration = distance_matrix['rows'][0]['elements'][0]['duration']['value']

            # Return distance and duration as a tuple
            return (distance, duration,)
        except Exception as e:
            # handle the exception
            print(f"An error occurred: {e}")
            return None
