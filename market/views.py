from django.utils import timezone
import json
from time import time
from django.http import JsonResponse
from django.shortcuts import render
from authentication.models import User
from market.models import Product, TransactionHistory
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/')
def show_market(request):
    return render(request, 'market.html')

@login_required(login_url='/')
def get_products(request):
    page_number = request.GET.get('page')
    
    products = Product.objects.all()
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
    
def order_transactions(request):
    bodyRequest = json.loads(request.body.decode("utf-8"))
    
    products = Product.objects.filter(id=bodyRequest.get('productId'))
    user = User.objects.get(pk=request.user.id)
    
    amount = bodyRequest.get('amount')

    if len(products) == 1:
        product = products[0]
        product.stock = product.stock - amount
        product.save()
        
        
        remainder = user.coin_amount - (product.price * amount)
        if remainder >= 0:
            user.coin_amount = remainder
            user.save()
            
            transaction_history_instance = TransactionHistory(user = request.user, product = product, amount = amount, date=timezone.now())
            transaction_history_instance.save()
            
            bodyResponse = {
                "success": True,
                "content": None,
                "message": "Transaction success"
            }
        else: 
            bodyResponse = {
                "success": False,
                "content": None,
                "message": "Insufficient coin"
            }
    else:
        bodyResponse = {
            "success": False,
            "content": None,
            "message": "Product not found"
        }
        
    json_object = json.dumps(bodyResponse, indent = 4) 
    return JsonResponse(json.loads(json_object))
    