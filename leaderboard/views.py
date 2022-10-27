from django.shortcuts import render
from leaderboard.models import Task

def show_leaderboard(request):
    context = {}
    return render(request, 'leaderboard.html', context)
# Create your views here.
