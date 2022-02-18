from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from customer.views.customer import CustomerView
from customer.views.vehicle import VehicleView

urlpatterns = [
    path('customer', CustomerView.as_view()),
    path('vehicle', VehicleView.as_view()),
]
