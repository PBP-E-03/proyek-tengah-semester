from django.db import models
from authentication.models import User

class UserStatsSummary(models.Model):
    most_donated_country = models.CharField(max_length=100, null=True)
    total_donated_tree = models.IntegerField(default=0)
    synced = models.BooleanField(default=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
class UserStats(models.Model):
    donation_amount = models.IntegerField()
    country_code = models.CharField(max_length=100)
    user_stats_summary = models.ForeignKey(UserStatsSummary, on_delete=models.CASCADE, default=None)
