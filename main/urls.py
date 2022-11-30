from django.urls import path

from main.views import get_country, get_region

app_name = 'main'

urlpatterns = [
    path('location', get_country, name='get_country'),
    path('location/<str:country_code>', get_region, name='get_region'),
]