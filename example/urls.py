from django.urls import path
from example.views import show

app_name = 'example'

urlpatterns = [
    path('', show, name='show'),
]