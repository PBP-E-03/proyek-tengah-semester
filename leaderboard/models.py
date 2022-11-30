from django.db import models
from authentication.models import User


class UserStats(models.Model):
    donation_amount = models.IntegerField()
    country_code = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete =models.CASCADE)

# Create your models here.
