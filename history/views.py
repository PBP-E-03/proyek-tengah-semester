from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework import status

from donation.models import DonationHistory
from market.models import TransactionHistory

# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_history(request: Request):
    try:
        donation_histories = DonationHistory.objects.select_related('person').filter(user_id=request.user.id).order_by('-date')
        transaction_histories = TransactionHistory.objects.select_related('product').filter(user_id=request.user.id).order_by('-date')

        donation_history_list = []
        for donation_history in donation_histories:
            donation = {
                "amount": donation_history.amount,
                "country": donation_history.country,
                "date": donation_history.date,
            }
            
            if donation_history.person is not None:
                donation['person'] = donation_history.person.name
            else:
                donation['person'] = None
            donation_history_list.append(donation)
        
        transaction_history_list = []
        for transaction_history in transaction_histories:
            transaction = {
                "product_name": transaction_history.product.name,
                "product_amount": transaction_history.product_amount,
                "transaction_amount": transaction_history.transaction_amount,
                "date": transaction_history.date,
            }
            
            transaction_history_list.append(transaction)
            
        response = {
            "success": True,
            "content": {
                "donation_history": donation_history_list,
                "transaction_history": transaction_history_list
            },
            "message": "History successfully retrieved!"
        }
        
        return Response(data=response, status=status.HTTP_200_OK)
    except Exception as e:
        response = {
            "success": False,
            "content": None,
            "message": str(e)
        }
         
        return Response(data=response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)