from django.shortcuts import render
import market.models as models

# Create your views here.
def show_market(request):
    products = models.Product.objects.all()
    history = models.TransactionHistory.objects.all()
    context = {
        'list_products' : products,
        'transaction_history' : history,
    }
    return render(request, 'market.html', context)