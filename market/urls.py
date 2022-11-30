from django.urls import path
from market.views import get_products, order_transactions

app_name = 'market'

urlpatterns = [
    path('product', get_products, name="get_products"),
    path('transaction', order_transactions, name="transaction")
]