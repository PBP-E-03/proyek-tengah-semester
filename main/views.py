from urllib import response
from django.http import HttpResponse
from django.shortcuts import render
import requests

def index(request):
    return render(request, 'example.html')  

def get_country(request):
    response = requests.get("http://battuta.medunes.net/api/country/all/?key=e156eb48631da358df83b2219d80585d")
    return HttpResponse(response, { "content-type": "application/json"})

def get_region(request, country_code):
    response = requests.get(f'http://battuta.medunes.net/api/region/{country_code}/all/?key=e156eb48631da358df83b2219d80585d')
    return HttpResponse(response, { "content-type": "application/json"})
