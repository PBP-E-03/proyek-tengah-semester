from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=255, default=None)
    code = models.CharField(max_length=255, default=None)
    
class Region(models.Model):
    name = models.CharField(max_length=255, default=None)
    code = models.CharField(max_length=255, default=None)
