from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class CustomerVehicles(models.Model):
    customer_id = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    plate = models.CharField(max_length=10)
    class Kind(models.IntegerChoices):
        CARRO = 1
        MOTO = 2
    kind = models.IntegerField(choices=Kind.choices, null=True)

    def __str__(self):
        return self.plate
