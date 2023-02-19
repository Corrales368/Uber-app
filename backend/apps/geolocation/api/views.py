# Import django
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Import self app
from .serializers import AddressGeolocationSerializer
from ..utils import get_geocode_from_address


class GeolocationAPIView(APIView):
    """
    View that processes a POST request to geolocate an address
    and return its latitude and longitude
    """
    serializer_class = AddressGeolocationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
       
