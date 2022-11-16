import code
import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import requests
from django.middleware.csrf import rotate_token

from main.models import Country, Region

def index(request):
    rotate_token(request)
    return render(request, 'index.html')

def get_country(request):
    response = Country.objects.all().values()
    json_object = json.dumps(list(response), indent = 4) 

    return JsonResponse(json.loads(json_object), safe=False)

def get_region(request, country_code):
    response = Region.objects.filter(code=country_code).values()
    json_object = json.dumps(list(response), indent = 4) 

    return JsonResponse(json.loads(json_object), safe=False)
