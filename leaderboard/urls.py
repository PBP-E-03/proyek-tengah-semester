from django.urls import path
from leaderboard.views import show_leaderboard

app_name = "leaderboard"

urlpatterns = [
    path('', show_leaderboard, name = "leaderboard_home"),
]