from django.utils import timezone
import json
from time import time
from django.http import JsonResponse
from django.shortcuts import render
from authentication.models import User
from market.models import Product, TransactionHistory
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.request import Request

from market.serializers import TransactionHistorySerializer

# Create your views here.
@api_view(['GET'])
def get_products(request: Request):
    try:
        page_number = request.query_params['page']
    
        products = Product.objects.all()
        products_paginator = Paginator(products.order_by("id"), 12)
        page = products_paginator.page(page_number)
        
        response = {
            "success": True,
            "content": {
                    "totalPages": products_paginator.num_pages,
                    "products": list(page.object_list.values()),
                    "meta": {
                        "hasNextPage": page.has_next(),
                        "hasPrevPage": page.has_previous(),
                    }
                },
            "message": "Products in page " + str(page_number) + " successfully retrieved!"
        }
        
        return Response(data=response, status=status.HTTP_200_OK)
    except Exception as e:
        response = {
            "success": False,
            "content": None,
            "message": str(e)
        }
        
        
        return Response(data=response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def order_transactions(request: Request):
    try:
        data = request.data
    
        product = Product.objects.get(id=data['product_id'])
        
        product_amount = data['product_amount']
        transaction_amount = product.price * product_amount
        
        if product.stock < product_amount:
            raise Exception('Insufficient stock')

        product.stock = product.stock - product_amount
        
        remainder = request.user.coin_amount - transaction_amount
        
        if remainder < 0:
            raise Exception('Insufficient coin')
        
        request.user.coin_amount = remainder
        
        transaction_data = {
            "user": request.user.id,
            "product": product.id,
            "product_amount": product_amount,
            "transaction_amount": transaction_amount,
            "date": timezone.now()
        }
        
        serializer = TransactionHistorySerializer(data=transaction_data)

        if serializer.is_valid():
            request.user.save()
            product.save()
            serializer.save()
        
        response = {
            "success": True,
            "content": None,
            "message": "Transaction success!"
        }
        
        return Response(data=response, status=status.HTTP_200_OK)
    except Exception as e:
        response = {
            "success": False,
            "content": None,
            "message": str(e)
        }
        
        
        return Response(data=response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    