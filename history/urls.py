from django.urls import path

from history.views import get_history

app_name = "history"

urlpatterns = [
    path('', get_history, name="get_history"),
]