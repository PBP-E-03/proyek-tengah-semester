from django.urls import path

from main.views import get_country, get_user

app_name = 'main'

urlpatterns = [
    path('location', get_country, name='get_country'),
    path('user', get_user, name='get_user'),
]