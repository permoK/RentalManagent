# models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    LANDLORD = 'landlord'
    TENANT = 'tenant'
    ROLE_CHOICES = [
        (LANDLORD, 'Landlord'),
        (TENANT, 'Tenant'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.username} - {self.role} - {self.phone_number}"
    
class LandlordProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100, blank=True)
    registration_number = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.user} - {self.company_name} - {self.registration_number}"

class TenantProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    emergency_contact = models.CharField(max_length=20, blank=True)
    id_number = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"{self.user} - emergency_contact {self.emergency_contact} - id {self.id_number}"
