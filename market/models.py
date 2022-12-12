from django.db import models
from authentication.models import User
from django.utils import timezone

# Create your models here.
class Product(models.Model):
    image = models.ImageField(upload_to='product-image', default=None)
    name = models.CharField(max_length=255)
    stock = models.IntegerField()
    price = models.IntegerField()

class TransactionHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_amount = models.IntegerField(default=None)
    transaction_amount = models.IntegerField(default=None)
    date = models.DateTimeField(default=timezone.now)
