from django.urls import path
from market.views import get_products, order_transactions, show_market

app_name = 'market'

urlpatterns = [
    path('', show_market, name='market_home'),
    path('product', get_products, name="get_products"),
    path('transaction', order_transactions, name="transaction")
]