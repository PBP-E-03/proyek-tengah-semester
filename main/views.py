from rest_framework.decorators import api_view
from rest_framework.response import Response
from leaderboard.models import UserStats, UserStatsSummary
from main.models import Country
from rest_framework import status
from rest_framework.request import Request

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

@api_view(['GET'])
def get_user(request: Request):
    try:
        user_stats_summary =  UserStatsSummary.objects.filter(id=request.user.id).first()
        most_donated_country = user_stats_summary.most_donated_country
        
        if not user_stats_summary.synced:
            user_stats = UserStats.objects.filter(user_stats_summary_id=user_stats_summary.id)
        
            most_donated_amount = 0
            most_donated_country_code = ""
            for user_stat in user_stats:
                if user_stat.donation_amount > most_donated_amount:
                    most_donated_amount = user_stat.donation_amount
                    most_donated_country_code = user_stat.country_code
            
            country = Country.objects.filter(code=most_donated_country_code).first()
            most_donated_country = country.name
            user_stats_summary.most_donated_country = country.name
            user_stats_summary.synced = True
            user_stats_summary.save()
            
        user_name_words = request.user.username.split(' ')
        if len(user_name_words) >= 3:
            last_name = user_name_words[2][0]
            user_name_words = [
                user_name_words[0],
                user_name_words[1],
                last_name
            ]
        
        user_name = " ".join(user_name_words)
        
        response = {
            "success": True,
            "content": {
                "name": user_name,
                "email": request.user.email,
                "coin": request.user.coin_amount,
                "total_donated_tree": user_stats_summary.total_donated_tree,
                "most_donated_country": most_donated_country
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