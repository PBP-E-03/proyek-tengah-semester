from django.shortcuts import render

def show_leaderboard(request):
    context = {}
    return render(request, 'leaderboard.html', context)
# Create your views here.
