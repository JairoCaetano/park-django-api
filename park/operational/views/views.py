from django.views.generic import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.utils import timezone
import json

from operational.models import ParkMovement
from customer.models import CustomerVehicles, Customer

@method_decorator(csrf_exempt, name='dispatch')
class MovementView(View):
    def post(self, request, *agrs, **kwargs):
        body = json.loads(request.body)
        try:
            vehicle = CustomerVehicles.objects.get(plate=body['plate'])
            if not vehicle:
                vehicle_id = CustomerVehicles.objects.create(
                plate=body['plate']).id
            movement = ParkMovement(entry_date=body['entry_date'], plate=body['plate'])
            movement.save()

            res = {
                'success': True,
                'plate:' : body['plate'],
                'message': "POST | class MovementView(View)"
            }
        except Exception as e:
            res = {
                'success': False,
                'message': "POST | class MovementView(View)",
                'Exception': str(e)
            }
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

