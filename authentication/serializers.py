import datetime
from rest_framework import serializers
from rest_framework.validators import ValidationError
from authentication.models import User

class RegistrationSerializer(serializers.ModelSerializer):
    password_confirmation = serializers.CharField()
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'phone', 'address', 'password_confirmation']
 
    def validate(self, attrs):
        if attrs["password"] != attrs["password_confirmation"]:
            raise ValidationError("Password didn't match")
        
        return super().validate(attrs)
    
    def create(self, validated_data):
        validated_data.pop("password_confirmation")
        password = validated_data.pop("password")
        
        user = super().create(validated_data)
        
        user.set_password(password)
        
        user.save()
        
        return user 
