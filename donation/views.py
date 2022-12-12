import json
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from donation.serializers import DonationHistorySerializer, PersonSerializer
from leaderboard.models import UserStats, UserStatsSummary
from leaderboard.serializers import UserStatsSerializer
from main.models import Country

@api_view(['POST'])    
def submit_donation(request: Request):
    try:
        data = request.data
        
        amount = int(data['amount'])
    
        rewarded_coins = amount * 100
        
        is_for_someone = data["donate_for_someone"] 
        
        if is_for_someone and data.get('person') is None:
            raise Exception("Person data is required!")
        
        country = Country.objects.get(code=data['country_code'])
        
        donation_history_data = {
            "user": request.user.id,
            "amount": amount,
            "rewarded_coins": rewarded_coins,
            "country": country.name,
            "hopes": data["hopes"],
            "donate_for_someone": is_for_someone,
        }
                
        donation_history_serializer = DonationHistorySerializer(data=donation_history_data)
        
        request.user.coin_amount = request.user.coin_amount + rewarded_coins
        
        user_stats_summary = UserStatsSummary.objects.filter(user=request.user).first()
        
        if user_stats_summary is None:
            raise Exception("User stats summary not found!")
        
        user_stats = UserStats.objects.filter(country_code=country.code, user_stats_summary=user_stats_summary)
        
        donation_history = None
        
        user_stats_summary.total_donated_tree = user_stats_summary.total_donated_tree + amount
        user_stats_summary.synced  = False
        
        if user_stats.first() is None:
            user_stats_data = {
                "donation_amount": amount,
                "country_code": country.code,
                "user_stats_summary": user_stats_summary.pk
            }
            
            user_stats_serializer = UserStatsSerializer(data=user_stats_data)
            
            if user_stats_serializer.is_valid() and donation_history_serializer.is_valid():
                donation_history = donation_history_serializer.save()
                user_stats_serializer.save()
                user_stats_summary.save()
            else:
                print("User Stats error:", user_stats_serializer.errors)
                print("Donation error:", donation_history_serializer.errors)
                raise Exception("user stats or donation error")
                
        else:
            user_stats = user_stats.first()
            user_stats.donation_amount = user_stats.donation_amount + amount
            if donation_history_serializer.is_valid():
                donation_history = donation_history_serializer.save()
                user_stats.save()
                user_stats_summary.save()
            else:
                print("Donation error:", donation_history_serializer.errors)
                raise Exception("donation error")
                
        request.user.save()
        
        if is_for_someone:
            person_data=json.loads(data['person'])
            person_serializer = PersonSerializer(data=person_data)
            if person_serializer.is_valid():
                person = person_serializer.save()
                donation_history.person = person
                donation_history.save()
            else:
                print("Person error:", person_serializer.errors)
                raise Exception("Provided person data is not valid!")
        
        response = {
            "success": True,
            "content": None,
            "message": "Donation success!"
        }
        
        return Response(data=response, status=status.HTTP_201_CREATED)
    except Exception as e:
        print(e)
        response = {
            "success": False,
            "content": None,
            "message": str(e)
        }
         
        return Response(data=response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
