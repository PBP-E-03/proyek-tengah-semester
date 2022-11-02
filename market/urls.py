from django.urls import path
from market.views import get_products, show_market

app_name = 'market'

urlpatterns = [
    path('', show_market, name='market_home'),
    path('product', get_products, name="get_products")
]