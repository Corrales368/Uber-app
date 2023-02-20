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
        self.matrix = None  # Initially not have a result of the distance matrix

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

    def get_matrix_from_coords(self, lat1, lng1, lat2, lng2):
        """
        Get distance and duration from origin coordinates to destination coordinates
        """
        try:
            # Define origin and destination coordinates
            origin = f"{lat1},{lng1}"
            destination = f"{lat2},{lng2}"

            # Get distance matrix 
            distance_matrix = self.gmaps.distance_matrix(origin, destination)

            # Save result for later use
            self.matrix = distance_matrix
        except Exception as e:
            # Handle the exception
            print(f"An error occurred: {e}")
            return None
    
    @property
    def get_distance(self):
        """
        Get distance from origin coordinates to destination coordinates
        """
        if self.matrix is not None:
            # Extract distance and distance from response
            return self.matrix['rows'][0]['elements'][0]['distance']['value']
        else:
            print("Matrix is not available yet.")
            return None

    @property
    def get_duration(self):
        """
        Get duration from origin coordinates to destination coordinates
        """
        if self.matrix is not None:
            # Extract distance and duration from response
            return self.matrix['rows'][0]['elements'][0]['duration']['value']
        else:
            print("Matrix is not available yet.")
            return None
