from django.views.generic import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json

from customer.models import Customer



@method_decorator(csrf_exempt, name='dispatch')
class CustomerView(View):
    def post(self, request, *agrs, **kwargs):
        body = json.loads(request.body)
        customer = Customer(name=body['name'])
        res = {
            'success': True,
            'name:' : body['name'],
            'message': "POST | class CustomerView(View)"
        }
        customer.save()
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

