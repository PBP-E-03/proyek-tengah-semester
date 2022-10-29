from django.urls import path

from donation.views import show_donation, submit_donation, get_donations_json

app_name = "donation"

urlpatterns = [
    path('', show_donation, name="show_donation"),
    path('submit/', submit_donation, name="submit_donation"),
    path('json/', get_donations_json, name="get_donations_json"),
]