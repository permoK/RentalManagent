# models.py
from django.db import models
from authentication.models import User

class Property(models.Model):
    landlord = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.landlord.username}"

class UnitType(models.Model):
    name = models.CharField(max_length=50)  # e.g., "1 Bedroom", "Bedsitter"
    default_rent = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.default_rent}"

class Unit(models.Model):
    STATUS_CHOICES = [
        ('occupied', 'Occupied'),
        ('available', 'Available'),
    ]
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    unit_type = models.ForeignKey(UnitType, on_delete=models.CASCADE)
    unit_number = models.CharField(max_length=20)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    tenant = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    lease_start = models.DateField(null=True, blank=True)
    lease_end = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.property.name} - Unit {self.unit_number}"

