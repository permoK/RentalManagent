# rentals/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PropertyViewSet, UnitViewSet, UnitTypeViewSet

# Create a router and register the viewsets
router = DefaultRouter()
router.register(r'properties', PropertyViewSet, basename='property')
router.register(r'units', UnitViewSet, basename='unit')
router.register(r'unit-types', UnitTypeViewSet, basename='unit-type')

urlpatterns = [
    # Include the router-generated URLs
    path('', include(router.urls)),
]
