from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from authentication.views import email_validation, logout, registration


app_name = 'authentication'

urlpatterns = [
    path('registration', registration, name='registration'),
    path('email-validation', email_validation, name='email-validation'),
    path('login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout', logout, name='logout'),
]