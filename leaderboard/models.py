from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    donation_amount = models.IntegerField()
    country = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete =models.CASCADE)

# Create your models here.
