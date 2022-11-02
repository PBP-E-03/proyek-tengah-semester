from django.shortcuts import render
from leaderboard.models import UserStats
from django.http import HttpResponse
from django.core import serializers

def show_leaderboard(request, country_code):
    context = {}
    return render(request, 'leaderboard.html', context)
# Create your views here.

def get_leaderboard(request, country):
    leaderboard = UserStats.objects.filter(country = country)
    return HttpResponse(serializers.serialize('json', leaderboard), content_type="application/json")
