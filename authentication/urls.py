# authentication/urls.py
from django.urls import path
from .views import (
    LandlordRegistrationView,
    TenantRegistrationView,
    CustomTokenObtainPairView,
)

urlpatterns = [
    # Landlord registration endpoint
    path('register/landlord/', LandlordRegistrationView.as_view(), name='landlord-register'),
    
    # Tenant registration endpoint
    path('register/tenant/', TenantRegistrationView.as_view(), name='tenant-register'),
    
    # Login endpoint (JWT token authentication)
    path('login/', CustomTokenObtainPairView.as_view(), name='token-obtain-pair'),
]
