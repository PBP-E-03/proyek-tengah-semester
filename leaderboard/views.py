from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from leaderboard.models import UserStats, UserStatsSummary
from rest_framework import status
from main.models import Country

@api_view(['GET'])
def get_leaderboard_by_country(request: Request, country_code):
    try:
        user_stats = UserStats.objects.filter(country_code = country_code).order_by('-donation_amount').values()
        
        user_stats_list = list(user_stats)
        leaderboards = user_stats_list[:5]
        rank = 0
        
        user_stats_summary = UserStatsSummary.objects.filter(user=request.user).first()
        
        for i in range(len((user_stats_list))):
            if user_stats_summary.pk == user_stats_list[i]['user_stats_summary_id']:
                rank = i + 1
                leaderboards.append(user_stats_list[i])
        
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
    
@api_view(['GET'])
def get_leaderboard(request: Request):
    try:
        countries = Country.objects.all().values()
        user_stats_summary_list = UserStatsSummary.objects.all().order_by('-total_donated_tree').values()
        
        leaderboards = list(user_stats_summary_list)[:5]
        rank = 0
        user_stats_summary = None

        for i in range(len((user_stats_summary_list))):
            if request.user.pk == user_stats_summary_list[i]['user_id']:
                rank = i + 1
                leaderboards.append(user_stats_summary_list[i])
                user_stats_summary = user_stats_summary_list[i]
        
        most_donated_country = user_stats_summary.get("most_donated_country") 
                
        if not user_stats_summary.get('synced'):
            user_stats = UserStats.objects.filter(user_stats_summary_id=user_stats_summary.get('id'))
            user_stats_summary = UserStatsSummary.objects.filter(id=user_stats_summary.get('id')).first()
        
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
            
        response = {
            "success": True,
            "content": {
                "rank": rank,
                "countries": countries,
                "lederboards": leaderboards,
                "most_donated_country": most_donated_country
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