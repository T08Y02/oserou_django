from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class PlayerUser(AbstractUser):
    pass

class Result(models.Model):
    score = models.IntegerField()
    winner_id = models.ForeignKey(PlayerUser, on_delete=models.CASCADE, related_name = "winner")
    loser_id = models.ForeignKey(PlayerUser, on_delete=models.CASCADE, related_name = "loser")
    created_at = models.DateTimeField()
    deleated_at = models.DateTimeField(null=True)


