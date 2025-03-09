# views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Property, UnitType, Unit
from .serializers import PropertySerializer, UnitTypeSerializer, UnitSerializer

class PropertyViewSet(viewsets.ModelViewSet):
    serializer_class = PropertySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Property.objects.filter(landlord=self.request.user)

    def perform_create(self, serializer):
        serializer.save(landlord=self.request.user)

class UnitViewSet(viewsets.ModelViewSet):
    serializer_class = UnitSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Unit.objects.filter(property__landlord=self.request.user)

class UnitTypeViewSet(viewsets.ModelViewSet):
    serializer_class = UnitTypeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return UnitType.objects.filter(property__landlord=self.request.user)
