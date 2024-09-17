from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json 
def f(request):
    return  JsonResponse({'message': 'accepted'})
@csrf_exempt
def add(request):
    if request.method == 'POST':
        data = json.loads(request.body)
       
        return JsonResponse({'message': data})