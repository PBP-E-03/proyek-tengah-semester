from django.shortcuts import render

# Create your views here.
def show_market(request):
    context = {}
    return render(request, 'market.html', context)