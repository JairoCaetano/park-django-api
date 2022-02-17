from django.views.generic import View
from django.http import Http404, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json

from customer.models import Customer

@method_decorator(csrf_exempt, name='dispatch')
class CustomerView(View):
    def post(self, request, *agrs, **kwargs):
        body = json.loads(request.body)
        try:
            customer = Customer(name=body['name'])
            customer.save()
            res = {
                'success': True,
                'name:' : body['name'],
                'message': "POST | class CustomerView(View)"
            }
        except:
            res = {
                'success': False,
                'message': "POST | class CustomerView(View)"
            }
        return JsonResponse(res)

    def put(self, request, *agrs, **kwargs):
        body = json.loads(request.body)
        try:
            customer = Customer.objects.get(pk=body['id'])
            customer.name = body['name']
            customer.save()
            res = {
                'success': True,
                'name:' : body['name'],
                'message': "PUT | class CustomerView(View)",
            }
        except:
            raise Http404(f"No id matches the given query. Id = {body['id']}")
        return JsonResponse(res)

