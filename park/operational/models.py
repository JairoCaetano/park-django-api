from django.db import models
from customer.models import CustomerVehicles
# Create your models here.
class ParkMovement(models.Model):
    entry_date = models.DateTimeField(auto_now_add=False, null=True)
    exit_date = models.DateTimeField(auto_now_add=False, null=True)
    validate_date = models.DateTimeField(auto_now_add=False, null=True)
    value = models.DecimalField(null=True, max_digits=10, decimal_places=2)
    plate = models.CharField(max_length=10)
    vehicle_id = models.ForeignKey(
        CustomerVehicles, null=True, on_delete=models.SET_NULL
    )
    def __str__(self):
        return self.plate

