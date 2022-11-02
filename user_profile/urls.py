from django.urls import path

from user_profile.views import index, update_password, update_profile

app_name = 'user_profile'

urlpatterns = [
    path('', index, name='profile'),
    path('update', update_profile, name='update_profile'),
    path('update-password', update_password, name='update_password'),
]