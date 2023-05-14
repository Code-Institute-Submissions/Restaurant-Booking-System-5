from django.db import models

# Create your models here.
class Slot(models.Model):
    day = models.DecimalField(null=False)
    time = models.DecimalField(null=False)
    booked = models.BooleanField(default=False)