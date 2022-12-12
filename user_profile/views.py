import json
from django.http import HttpResponseNotAllowed, JsonResponse
from rest_framework.response import Response
from authentication.models import User
from user_profile.forms import PasswordForm, ProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, permission_classes
from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from user_profile.serializers import UserPasswordSerializer, UserProfileSerializer
# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def index(request: Request):
    try:
        response = {
            "success": True,
            "content": {
                "username": request.user.username,
                "email": request.user.email,
                "phone": request.user.phone,
                "address": request.user.address
            },
            "message": "User successfully retrieved!"
        }
        
        return Response(data=response, status=status.HTTP_200_OK)
    except Exception as e:
        response = {
            "success": False,
            "content": None,
            "message": str(e)
        }
         
        return Response(data=response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_profile(request: Request):
    try:
        user = User.objects.get(pk=request.user.id)
        
        user_profile_serializer = UserProfileSerializer(instance=user, data=request.data, partial=True)

        if user_profile_serializer.is_valid():
            user_profile_serializer.save()

            response = {
                "success": True,
                "content": user_profile_serializer.data,
                "message": "Successfully updated",
            }
            return Response(data=response, status=status.HTTP_200_OK)
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
            "message": str(e)
        }
         
        return Response(data=response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_password(request: Request):
    try:
        user_password_serializer = UserPasswordSerializer(data=request.data)
        if user_password_serializer.is_valid():
            user = authenticate(request, email=request.user.email, password=user_password_serializer.data.get('current_password'))
            if user is not None:
                user.set_password(user_password_serializer.data.get('password'))
                user.save()
                response = {
                    "success": True,
                    "content": None,
                    "message": "Successfully updated"
                }
                return Response(data=response, status=status.HTTP_200_OK)

            else:
                response = {
                    "success": False,
                    "content": None,
                    "message": "Wrong password"
                }
                return Response(data=response, status=status.HTTP_400_BAD_REQUEST)

        else:
            print(user_password_serializer.errors)
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
            "message": str(e)
        }
         
        return Response(data=response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)