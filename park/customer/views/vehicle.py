from django.views.generic import View
from django.http import Http404, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json

from customer.models import Customer, CustomerVehicles

@method_decorator(csrf_exempt, name='dispatch')
class VehicleView(View):
    def post(self, request, *agrs, **kwargs):
        body = json.loads(request.body)
        try:
            vehicle = Customer.objects.get(pk=body['customer_id'])
            vehicle.customervehicles_set.create(
                plate=body['plate'],
                kind=body['kind']
            )
            vehicle.save()
            res = {
                'success': True,
                'id:' : body['customer_id'],
                'message': f'Sucess to register vehicle {body}',
            }
        except:
            return HttpResponse(f'Failed to register vehicle {body}', status=400)
        return (HttpResponse(JsonResponse(res), status=201))

    def put(self, request, *agrs, **kwargs):
        body = json.loads(request.body)
        try:
            vehicle = CustomerVehicles.objects.get(id=body['id'])
            if "plate" in body:
                vehicle.plate = body['plate']
            if "kind" in body:
                vehicle.kind = body['kind']
            vehicle.save()
            res = {
                'success': True,
                'id:' : body['id'],
                'message': f'Sucess to register vehicle {body}',
            }
        except Exception as e:
            return HttpResponse(f'No id matches the given query. Id = {body["id"]}', status=400)
        return (HttpResponse(JsonResponse(res), status=200))

