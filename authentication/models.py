from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager
# Create your models here.
class User(AbstractBaseUser):
    name = models.CharField(max_length=255, default=None)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.EmailField(max_length=254, unique=True)
    coin_amount = models.IntegerField(default=0)
    
    USERNAME_FIELD =  'email'

    objects = UserManager()
    
    def get_name(self):
        return self.name