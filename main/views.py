import code
import json
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from main.models import Country, Region
from rest_framework import status

@api_view(['GET'])
def get_country(request):
    try:
        countries = Country.objects.all().values()
        
        response = {
            "success": True,
            "content": {
                "countries": list(countries)
            },
            "message": "Countries successfully retrieved!"
        }
        
        return Response(data=response, status=status.HTTP_200_OK)
    except Exception as e:
        response = {
            "success": False,
            "content": None,
            "message": str(e)
        }
         
        return Response(data=response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

def get_region(request, country_code):
    response = Region.objects.filter(code=country_code).values()
    json_object = json.dumps(list(response), indent = 4) 

    return JsonResponse(json.loads(json_object), safe=False)
