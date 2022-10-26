from django.urls import path

from main.views import get_country, get_region, index

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('battuta/country', get_country, name='get_country'),
    path('battuta/<str:country_code>', get_region, name='get_region'),
]