from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Slot(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    day = models.CharField(null=False, max_length=10)
    time = models.DecimalField(null=False, decimal_places=2, max_digits=5)
    booked = models.BooleanField(default=False)
