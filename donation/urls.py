from django.urls import path

from donation.views import submit_donation

app_name = "donation"

urlpatterns = [
    path('', submit_donation, name="submit_donation"),
]