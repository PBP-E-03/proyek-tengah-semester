from django.urls import path

from donation.views import show_donation, submit_donation

app_name = "donation"

urlpatterns = [
    path('', show_donation, name="show_donation"),
    path('submit/', submit_donation, name="submit_donation"),
]