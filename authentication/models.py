from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager, BaseUserManager, PermissionsMixin

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, default=None)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.EmailField(max_length=254, unique=True)
    coin_amount = models.IntegerField(default=0)

    is_staff = models.BooleanField(default=False) # a admin user; non super-user
    is_superuser = models.BooleanField(default=False) # a superuser
    
    USERNAME_FIELD =  'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def get_name(self):
        return self.username
    
    def get_coin(self):
        return self.coin_amount