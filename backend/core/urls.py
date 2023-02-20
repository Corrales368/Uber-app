# Import django
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions

# Third apps
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view_v1 = get_schema_view(
   openapi.Info(
      title="Uber App",
      default_version='v1',
      description="Uber app docs version 1.0",
      terms_of_service="https://corralesdev.com",
      contact=openapi.Contact(email="santi368444110@gmail.cm"),
      license=openapi.License(name="Free"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view_v1.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view_v1.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('', include('apps.geolocation.api.routers')),
    path('', include('apps.driver.api.routers')),
    path('', include('apps.service.api.routers')),
]
