# Import django
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Import self app
from .serializers import DriverLocationSerializer
from ..models import Driver, DriverLocation


class LastLocationDriver(APIView):
    """
    View to get the last location of a driver
    """
    serializer_class = DriverLocationSerializer
    
    def post(self, request, *args, **kwargs):
        # Get session driver
        driver = Driver.objects.filter(user=request.user).first()
        # Validate driver if exist
        if driver is not None:
            try:
                location = driver.driverlocation
            except DriverLocation.DoesNotExist:
                location = None
            serializer = self.serializer_class(data=request.data, instance=location)
            if serializer.is_valid():
                serializer.save(driver=driver)
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"Driver not found"}, status=status.HTTP_404_NOT_FOUND)
