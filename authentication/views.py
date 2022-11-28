from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from authentication.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

from authentication.serializers import RegistrationSerializer

# Create your views here.
@api_view(['POST'])
def email_validation(request: Request):
    try:
        email = request.data.get('email')
        is_exist = True
        
        if email is not None:
            user = User.objects.filter(email = email).first()
            
            if user is None:
                is_exist = False

            response = {
                "success": True,
                "content": {
                    "is_exist": is_exist
                },
                "message": "User already exists!" if is_exist else "User not found!",
            }
            return Response(data=response, status=status.HTTP_200_OK)
        else:
            response = {
                "success": False,
                "content": None,
                "message": "Email is required!",
            }
            return Response(data=response, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        response = {
                "success": False,
                "content": None,
                "message": str(e),
            }
        return Response(data=response, status=status.HTTP_500_INTERNAL_SERVER_ERROR) 

@api_view(['POST'])    
def registration(request: Request):
    try:
        serializer = RegistrationSerializer(data=request.data)
    
        if serializer.is_valid():
            user = serializer.save()
            
            token = RefreshToken.for_user(user)

            response = {
                "success": True,
                "content": {
                    "refresh": str(token),
                    "access": str(token.access_token)    
                },
                "message": "Successfully registered",
            }
            return Response(data=response, status=status.HTTP_201_CREATED)
        else:
            response = {
                "success": False,
                "content": None,
                "message": "Missing required information!",
            }
            return Response(data=response, status=status.HTTP_400_BAD_REQUEST) 
    except Exception as e:
        response = {
                "success": False,
                "content": None,
                "message": str(e),
            }
        return Response(data=response, status=status.HTTP_500_INTERNAL_SERVER_ERROR) 
    
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout(request: Request):
    try:
        refresh_token = request.data["refresh"]
        token = RefreshToken(refresh_token)
        token.blacklist()
        
        response = {
                "success": True,
                "content": None,
                "message": "Successfully logged out",
            }

        return Response(data=response, status=status.HTTP_205_RESET_CONTENT)
    except Exception as e:
        response = {
                "success": False,
                "content": None,
                "message": str(e),
            }
        return Response(data=response, status=status.HTTP_500_INTERNAL_SERVER_ERROR) 
