# views.py
from rest_framework import generics, permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import (
    LandlordRegistrationSerializer,
    TenantRegistrationSerializer,
    CustomTokenObtainPairSerializer
)

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class LandlordRegistrationView(generics.CreateAPIView):
    serializer_class = LandlordRegistrationSerializer
    permission_classes = [permissions.AllowAny]

class TenantRegistrationView(generics.CreateAPIView):
    serializer_class = TenantRegistrationSerializer
    permission_classes = [permissions.AllowAny]
