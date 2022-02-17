from django.db import models

# Create your models here.
from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.nome

class CustomerVehicles(models.Model):
    customer_id = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    plate = models.CharField(max_length=10)
    kind = models.IntegerChoices('Kind', 'CARRO MOTO')

    def __str__(self):
        return self.plate
