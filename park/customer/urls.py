from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from customer.views import CustomerView

urlpatterns = [
    path('', CustomerView.as_view()),
]
