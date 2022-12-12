from rest_framework import serializers
from rest_framework.validators import ValidationError
from authentication.models import User

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'address']
 
class UserPasswordSerializer(serializers.ModelSerializer):
    password_confirmation = serializers.CharField()
    current_password = serializers.CharField()
    
    class Meta:
        model = User
        fields = ['password', 'password_confirmation', 'current_password']
        
    def validate(self, attrs):
            if attrs["password"] != attrs["password_confirmation"]:
                raise ValidationError("Password didn't match")
            
            if attrs["password"] == attrs["current_password"]:
                raise ValidationError("Password can't be same with current password")
            
            return super().validate(attrs)
    
    
