# Import third apps
import googlemaps
import os

def get_geocode_from_address(address:str):
    """
    Get latitude and longitude from address.
    """
    # Create instance Google Maps
    gmaps = googlemaps.Client(key=os.getenv('GOOGLE_MAPS_API_KEY'))

    # Get coordinates from address as string format
    geocode_result = gmaps.geocode(address)
    
    return geocode_result