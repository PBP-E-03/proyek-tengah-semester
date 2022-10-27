from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    image_url = models.CharField()
    name = models.CharField()
    stock = models.IntegerField()
    price = models.IntegerField()

class TransactionHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField()
    date = models.DateField()