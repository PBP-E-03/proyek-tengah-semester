from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Person(models.Model):
    name = models.TextField(default=None, null=True, blank=True)
    phone = models.TextField(default=None,null=True, blank=True)
    email = models.EmailField(default=None,null=True, blank=True)

class Donation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    amount = models.IntegerField()
    region = models.TextField()
    country = models.TextField()
    hopes = models.TextField()
    donate_for_someone = models.BooleanField()
    person = models.OneToOneField(Person, on_delete=models.CASCADE, null=True, blank=True)
    payment = models.ImageField(upload_to='images', default=None, null=True, blank=True)



    
