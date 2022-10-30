from django.db import models
from authentication.models import User

# Create your models here.
class Product(models.Model):
    image_url = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    stock = models.IntegerField()
    price = models.IntegerField()

class TransactionHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField()
    date = models.DateField()