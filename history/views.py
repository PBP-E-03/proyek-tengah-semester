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
        donation_history = DonationHistory.objects.filter(user_id=request.user.id).order_by('-date').values()
        transaction_history = TransactionHistory.objects.filter(user_id=request.user.id).order_by('-date').values()
       
        response = {
            "success": True,
            "content": {
                "donation_history": donation_history,
                "transaction_history": transaction_history
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