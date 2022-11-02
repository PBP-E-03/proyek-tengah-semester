from django.http import HttpResponse
from django.shortcuts import render
import requests

def index(request):
    return render(request, 'index.html')

def get_country(request):
    response = requests.get("http://battuta.medunes.net/api/country/all/?key=d0daed3e6e5d17c42e803fafab5e603f")
    return HttpResponse(response, { "content-type": "application/json"})

def get_region(request, country_code):
    response = requests.get(f'http://battuta.medunes.net/api/region/{country_code}/all/?key=d0daed3e6e5d17c42e803fafab5e603f')
    return HttpResponse(response, { "content-type": "application/json"})
