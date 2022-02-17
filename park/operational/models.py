from django.db import models

# Create your models here.
class ParkMovement(models.Model):
    entry_date = models.DateTimeField(auto_now_add=True)
    exit_date = models.DateTimeField(auto_now_add=False)
    validate_date = models.DateTimeField(auto_now_add=False)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    plate = models.CharField(max_length=10)
    def __str__(self):
        return self.plate

