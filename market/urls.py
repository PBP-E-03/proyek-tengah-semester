from django.urls import path
from market.views import show_market

app_name = 'market'

urlpatterns = [
    path('', show_market, name='market_home'),
]