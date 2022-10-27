from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=100)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete =models.CASCADE)

# Create your models here.
