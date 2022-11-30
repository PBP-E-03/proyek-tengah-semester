from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from leaderboard.models import UserStats
from rest_framework import status

@api_view(['GET'])
def get_leaderboard_by_country(request: Request, country_code):
    try:
        user_stats = UserStats.objects.filter(country_code = country_code).order_by('-donation_amount').values()
        
        user_stats_list = list(user_stats)
        leaderboards = user_stats_list[:5]
        rank = 0
        
        for i in range(len((user_stats_list))):
            if request.user.id == user_stats_list[i]['user_id']:
                rank = i + 1
        
        response = {
            "success": True,
            "content": {
                "rank": rank,
                "lederboards": leaderboards,
            },
            "message": "Leaderboard successfully retrieved!"
        }
        
        return Response(data=response, status=status.HTTP_200_OK)
    except Exception as e:
        response = {
            "success": False,
            "content": None,
            "message": str(e)
        }
         
        return Response(data=response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    