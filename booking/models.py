from django.db import models

# Create your models here.


class Slot(models.Model):
    day = models.CharField(null=False, max_length=10)
    time = models.DecimalField(null=False, decimal_places=2, max_digits=5)
    booked = models.BooleanField(default=False)
