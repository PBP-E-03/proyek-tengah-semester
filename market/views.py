import json
from django.http import JsonResponse
from django.shortcuts import render
import market.models as models
from django.core.paginator import Paginator
from django.templatetags.static import static

# Create your views here.
def show_market(request):
    return render(request, 'market.html')

def get_products(request):
    page_number = request.GET.get('page')
    
    products = models.Product.objects.all()
    products_paginator = Paginator(products.order_by("id"), 12)
    page = products_paginator.page(page_number)
    
    bodyResponse = {
        "success": True,
        "content": {
                "totalPages": products_paginator.num_pages,
                "products": list(page.object_list.values()),
                "meta": {
                    "hasNextPage": page.has_next(),
                    "hasPrevPage": page.has_previous(),
                }
            },
        "message": ""
    }
        
        
    json_object = json.dumps(bodyResponse, indent = 4) 
    return JsonResponse(json.loads(json_object))
    
    