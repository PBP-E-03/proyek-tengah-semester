from django.urls import path

from authentication.views import auth_login, auth_logout, registration


app_name = 'main'

urlpatterns = [
    path('registration', registration, name='registration'),
    path('login', auth_login, name='login'),
    path('logout', auth_logout, name='logout'),
]