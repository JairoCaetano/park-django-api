from django.views.generic import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.utils import timezone
import json

from operational.models import ParkMovement
from customer.models import CustomerVehicles

@method_decorator(csrf_exempt, name='dispatch')
class MovementView(View):
    def post(self, request, *agrs, **kwargs):
        body = json.loads(request.body)
        movement = ParkMovement(
        exit_date = body['exit_date'],
        validate_date = body['validate_date'],
        value = body['value'],
        name=body['name']
            )
        if "vehicle_id" in body:
            movement.vehicle_id = body['vehicle_id']
        res = {
            'success': True,
            'name:' : body['name'],
            'message': "POST | class CustomerView(View)"
        }
        movement.save()
        return JsonResponse(res)

    def put(self, request, *agrs, **kwargs):
        body = json.loads(request.body)
        customer = Customer.objects.get(pk=body['id'])
        customer.name = body['name']
        res = {
            'success': True,
            'name:' : body['name'],
            'message': "PUT | class CustomerView(View)",
        }
        customer.save()
        return JsonResponse(res)

