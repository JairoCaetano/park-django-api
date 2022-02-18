from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from park.operational.views.views import MovementView

urlpatterns = [
    path('movement', MovementView.as_view()),
]
