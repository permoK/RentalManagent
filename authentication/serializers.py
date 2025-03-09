# serializers.py
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import User, LandlordProfile, TenantProfile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'role', 'phone_number')

class LandlordRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    company_name = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'phone_number', 'company_name')
        
    def create(self, validated_data):
        company_name = validated_data.pop('company_name')
        user = User.objects.create_user(
            role=User.LANDLORD,
            **validated_data
        )
        LandlordProfile.objects.create(user=user, company_name=company_name)
        return user

class TenantRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    emergency_contact = serializers.CharField(write_only=True)
    id_number = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'phone_number', 'emergency_contact', 'id_number')
        
    def create(self, validated_data):
        emergency_contact = validated_data.pop('emergency_contact')
        id_number = validated_data.pop('id_number')
        user = User.objects.create_user(
            role=User.TENANT,
            **validated_data
        )
        TenantProfile.objects.create(user=user, emergency_contact=emergency_contact, id_number=id_number)
        return user

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['user_id'] = user.id
        token['role'] = user.role
        token['username'] = user.username

        return token
