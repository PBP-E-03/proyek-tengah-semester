from django.urls import path
from leaderboard.views import  get_leaderboard, get_leaderboard_by_country

app_name = "leaderboard"

urlpatterns = [
    path('<str:country_code>', get_leaderboard_by_country, name = "get_leaderboard_by_country"),
    path('', get_leaderboard, name = "get_leaderboard"),
]