from django.db import models

from authentication.models import User

# Create your models here.

class Person(models.Model):
    name = models.TextField(default=None, null=True, blank=True)
    phone = models.TextField(default=None,null=True, blank=True)
    email = models.EmailField(default=None,null=True, blank=True)

class DonationHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    amount = models.IntegerField()
    rewarded_coins = models.IntegerField()
    country = models.TextField()
    hopes = models.TextField()
    donate_for_someone = models.BooleanField()
    person = models.OneToOneField(Person, on_delete=models.CASCADE, null=True, blank=True)
    payment_receipt = models.ImageField(upload_to='payment_receipt', default=None)
