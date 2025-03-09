from rest_framework import serializers
from .models import Property, UnitType, Unit
from authentication.serializers import UserSerializer

class PropertySerializer(serializers.ModelSerializer):
    landlord = UserSerializer(read_only=True)

    class Meta:
        model = Property
        fields = ('id', 'landlord', 'name', 'address')
        read_only_fields = ('landlord',)

class UnitTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitType
        fields = ('id', 'name', 'default_rent')

class UnitSerializer(serializers.ModelSerializer):
    property = PropertySerializer(read_only=True)
    property_id = serializers.IntegerField(write_only=True)
    unit_type = UnitTypeSerializer(read_only=True)
    unit_type_id = serializers.IntegerField(write_only=True)
    tenant = UserSerializer(read_only=True)
    tenant_id = serializers.IntegerField(write_only=True, required=False, allow_null=True)

    class Meta:
        model = Unit
        fields = (
            'id', 'property', 'property_id', 'unit_type', 'unit_type_id',
            'unit_number', 'status', 'tenant', 'tenant_id', 'lease_start', 'lease_end'
        )
        read_only_fields = ('property', 'unit_type', 'tenant')

class UnitCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = (
                'id', 'property', 'unit_type', 'unit_number', 
                'status', 'tenant', 'lease_start', 'lease_end'
                )
